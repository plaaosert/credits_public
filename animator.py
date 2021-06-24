class DataStoringObject:
    def __init__(self):
        self.data = {}

    def set_data(self, *ident):
        for i in range(0, len(ident), 2):
            self.data[ident[i]] = ident[i + 1]

    def get_data(self, ident):
        if ident in self.data:
            return self.data[ident]

    def oper_data(self, ident, oper):
        self.data[ident] = oper(self.data[ident])


class SceneManager(DataStoringObject):
    def __init__(self, scenes, events):
        super().__init__()

        self.scenes = {scene.name: scene for scene in scenes}
        self.events = {event.beat: [ev for ev in events if ev.beat == event.beat] for event in events}

        for scene in scenes:
            scene.set_parent(self)

        self.active_scene = []
        self.cur_beat = -1
        self.data = {}

    def start_scene(self, scene, at=0):
        if len(self.active_scene) == 0:
            self.active_scene.append(None)

        self.active_scene[0] = self.scenes[scene]
        self.active_scene[0].start(at)

    def add_scene(self, scene, at=0):
        self.active_scene.append(self.scenes[scene])
        self.active_scene[-1].start(at)

    def remove_scene(self, scene):
        if self.scenes[scene] in self.active_scene:
            self.active_scene.remove(self.scenes[scene])

    def request_next(self, render=True):
        for scene in self.active_scene:
            scene.request_frame(render)

        self.next_beat()

    def next_beat(self):
        self.cur_beat += 1
        if self.cur_beat in self.events:
            for event in self.events[self.cur_beat]:
                event.do(self)

    def set_scene_data(self, scene, *ident):
        self.scenes[scene].set_data(*ident)

    def set_generator_data(self, scene, generator, *ident):
        self.scenes[scene].generators[generator].set_data(*ident)


class Event:
    def __init__(self, beat, do):
        self.beat = beat
        self.do = do

    @staticmethod
    def swap_scene(sc, at=0):
        return lambda sm: sm.start_scene(sc, at)

    @staticmethod
    def layer_scene(sc, at=0):
        return lambda sm: sm.add_scene(sc, at)

    @staticmethod
    def remove_scene(sc):
        return lambda sm: sm.remove_scene(sc)


class Scene(DataStoringObject):
    def __init__(self, name, generators):
        super().__init__()

        self.parent = None
        self.name = name
        self.generators = generators
        self.start_beat = 0
        self.internal_beat = 0

    def set_parent(self, parent):
        self.parent = parent

    # Requests a frame. This basically calls the request() and request_clear() functions in every generator.
    def request_frame(self, render=True):
        beat = self.internal_beat
        if render:
            for generator in self.generators:
                if beat >= generator.start_beat and generator.condition(beat):
                    if beat != self.start_beat and beat != generator.start_beat:
                        # Clear previous beat
                        generator.request_clear(generator, beat - 1)

                    # Make current
                    generator.request(generator, beat)

        self.internal_beat += 1

    # Starts the scene at the beat given.
    def start(self, at):
        for generator in self.generators:
            generator.set_parent(self.parent)
            generator.set_scene(self)
            generator.on_create(generator)

        self.start_beat = at
        self.internal_beat = at
        self.request_frame()


class Generator(DataStoringObject):
    def __init__(self, start_beat, condition, on_create, request, request_clear):
        super().__init__()

        self.parent = None
        self.scene = None

        self.data = {}
        self.start_beat = start_beat
        self.condition = condition
        self.on_create = on_create
        self.request = request
        self.request_clear = request_clear

    def set_parent(self, parent):
        self.parent = parent

    def set_scene(self, scene):
        self.scene = scene

    @staticmethod
    def combine_conditions(*cond):
        return lambda b: all(c(b) for c in cond)

    @staticmethod
    def always():
        return lambda b: True

    @staticmethod
    def every_n_beats(beat):
        return lambda b: b % beat == 0

    @staticmethod
    def every_on_off(on, off):
        return lambda b: (b % (on + off)) < on

    @staticmethod
    def every_off_on(off, on):
        return lambda b: (b % (on + off)) >= off

    @staticmethod
    def before_n(beat):
        return lambda b: b < beat

    @staticmethod
    def at_beat(beat):
        return lambda b: b == beat

    @staticmethod
    def no_create():
        return lambda g: None

    @staticmethod
    def no_request():
        return lambda g, b: None
