from animation_functions import debug_info
from CLIRender.classes import enable_ansi
from colorama import Fore, Style

import keyboard
import time
import os
import random
from just_playback import Playback

from animation_scenes import all_scenes, canvas
from string_defs import data_strings

import animator as am

enable_ansi()
# canvas.render_blank()
delay = 60.0 / 179.0 / 8.0
beat = -60
offset = 5.492
# print((delay * 980) + offset)
skip_by = 0

debug = False
last_frames = []


def skip_beats(ctr, amount, next_debug):
    global beat
    global skip_by

    ctr.cur_beat += amount
    beat += amount

    if debug:
        controller.events[next_debug] = (am.Event(next_debug, am.Event.layer_scene("debug_counter")),)

    skip_by = offset + (delay * amount)


counter = am.Scene(
    "debug_counter",
    (
        am.Generator(
            0, am.Generator.always(),
            am.Generator.no_create(),
            lambda g, b: debug_info(canvas, g, b, last_frames),
            am.Generator.no_request()
        ),
    )
)


ocean_events = (
    am.Event(60, lambda c: c.set_generator_data(
        "ocean_b", 1, "text", data_strings["ocean_b_0"]
    )),
    am.Event(310, lambda c: c.set_generator_data(
        "ocean_b", 1,
        "text", "[##CLEAR|60;6"
    )),
    am.Event(310, lambda c: c.set_generator_data(
        "ocean_b", 0, "ocean_glitch", 3
    )),
    am.Event(310, lambda c: c.set_generator_data(
        "ocean_b", 0, "ocean_col", Style.NORMAL + Fore.BLUE
    )),
    am.Event(312, lambda c: c.set_generator_data(
        "ocean_b", 0, "ocean_col", Style.BRIGHT + Fore.BLUE
    )),
    am.Event(314, lambda c: c.set_generator_data(
        "ocean_b", 0, "ocean_col", Style.NORMAL + Fore.BLUE
    )),
    am.Event(320, lambda c: c.set_generator_data(
        "ocean_b", 1, "text", data_strings["ocean_b_1"], "offset", 0
    )),
    am.Event(590, lambda c: c.set_generator_data(
        "ocean_b", 0, "ocean_col", Style.BRIGHT + Fore.BLACK
    )),
    am.Event(646, lambda c: c.set_generator_data(
        "ocean_b", 1,
        "text", "[##CLEAR|60;8"
    )),
    am.Event(652, lambda c: c.set_generator_data(
        "ocean_b", 1,
        "text", data_strings["ocean_b_2"], "offset", 0
    )),
    am.Event(656, lambda c: c.set_generator_data(
        "ocean_b", 0, "ocean_col", Style.NORMAL + Fore.YELLOW
    )),
    am.Event(666, lambda c: c.set_generator_data(
        "ocean_b", 0, "ocean_col", Style.BRIGHT + Fore.YELLOW
    )),
    am.Event(666, lambda c: c.set_generator_data(
        "ocean_b", 0, "ocean_glitch", 6
    )),
    am.Event(850, lambda c: c.set_generator_data(
        "ocean_b", 0, "ocean_col", Style.NORMAL + Fore.YELLOW
    )),
    am.Event(999, lambda c: c.set_generator_data(
        "ocean_b", 1,
        "text", "[##CLEAR|60;10"
    )),
    am.Event(1000, lambda c: c.set_generator_data(
        "ocean_b", 0, "ocean_col", Style.BRIGHT + Fore.BLACK
    )),
    am.Event(1000, lambda c: c.set_generator_data(
        "ocean_b", 0, "ocean_glitch", 13
    )),
    am.Event(1000, lambda c: c.set_generator_data(
        "ocean_b", 1,
        "text", data_strings["ocean_b_3"],
        "offset", 0
    )),
    am.Event(1044, lambda c: c.set_generator_data(
        "ocean_b", 0, "ocean_glitch", 102
    )),
    am.Event(1048, lambda c: c.set_generator_data(
        "ocean_b", 0, "ocean_glitch", 230
    )),
    am.Event(1052, lambda c: c.set_generator_data(
        "ocean_b", 0, "ocean_glitch", 500
    )),
    am.Event(1056, lambda c: c.set_generator_data(
        "ocean_b", 0, "ocean_glitch", 760
    )),
    am.Event(1060, lambda c: c.set_generator_data(
        "ocean_b", 0, "ocean_glitch", 1600
    )),
    am.Event(1064, lambda c: c.set_generator_data(
        "ocean_b", 0, "ocean_glitch", 2500
    ))
)


ocean2_events = (
    am.Event(3896, lambda c: c.set_generator_data(
            "ocean_c", 1, "text", data_strings["ocean_c_0"]
        )
    ),
    am.Event(3896, lambda c: c.set_generator_data(
            "ocean_c", 2, "text", data_strings["ocean_c_1"]
        )
    ),

    am.Event(3896, lambda c: c.set_generator_data(
            "ocean_c", 3, "text", data_strings["ocean_c_2"]
        )
    ),

    am.Event(3896, lambda c: c.set_generator_data(
            "ocean_c", 4, "text", data_strings["ocean_c_3"]
        )
    ),

    am.Event(4400, lambda c: c.set_generator_data(
        "ocean_c", 1,
        "text", "[##CLEAR|60;10"
    )),

    *(
        am.Event(4401 + i * 2, lambda c: c.set_generator_data(
            "ocean_c", 0, "ocean_col", random.choice((Style.BRIGHT, Style.NORMAL)) + Fore.BLACK
        )) for i in range(5)
    ),

    am.Event(4411, lambda c: c.set_generator_data(
        "ocean_c", 0, "ocean_col", Style.NORMAL + Fore.BLACK
    )),
)


controller = am.SceneManager((*all_scenes, counter), (
    am.Event(0, am.Event.swap_scene("wipe")),
    # am.Event(1, am.Event.layer_scene("debug_counter")),
    am.Event(58, am.Event.swap_scene("clear")),
    am.Event(60, am.Event.swap_scene("ocean_b")),
    # am.Event(60, am.Event.layer_scene("typewrite")),
    *ocean_events,
    am.Event(1079, am.Event.swap_scene("clear")),
    am.Event(1080, am.Event.swap_scene("beats")),
    am.Event(1080, am.Event.layer_scene("title")),
    am.Event(1080, am.Event.swap_scene("beats")),
    am.Event(1336, am.Event.swap_scene("beats_lr")),
    am.Event(1844, am.Event.remove_scene("title")),
    am.Event(1848, am.Event.swap_scene("funding")),
    am.Event(1848, am.Event.layer_scene("dates")),
    am.Event(1848, am.Event.layer_scene("weather")),
    am.Event(1848, lambda c: c.set_data(
        "history", [], "refresh", True
    )),

    am.Event(1848, lambda c: c.set_generator_data(
        "funding", 0, "text", data_strings["funding_0"]
    )),

    am.Event(2348, lambda c: c.set_generator_data(
        "funding", 0, "text", (('',), ('',))
    )),

    am.Event(2348, lambda c: c.set_data(
        "history", [], "refresh", True
    )),

    am.Event(2352, lambda c: c.set_generator_data(
        "funding", 0, "text", data_strings["funding_1"], "offset", 0, "lineno", 0
    )),

    am.Event(2976, am.Event.remove_scene("dates")),
    am.Event(2976, am.Event.remove_scene("weather")),

    am.Event(2976, am.Event.swap_scene("clear_wipe")),
    am.Event(3007, am.Event.swap_scene("clear")),

    # idk what to do here. some sort of bootup sequence?
    am.Event(3132, am.Event.swap_scene("loadingbar")),
    am.Event(3132, lambda c: c.set_generator_data(
        "loadingbar", 6, "text", data_strings["funding_2"]
    )),

    am.Event(3376, am.Event.swap_scene("ocean_d")),
    am.Event(3380, am.Event.swap_scene("clear")),
    am.Event(3380, am.Event.swap_scene("fastload")),
    am.Event(3388, am.Event.swap_scene("clear")),

    # Crazy part. Go wild
    am.Event(3390, am.Event.swap_scene("error")),
    am.Event(3390, am.Event.layer_scene("fundingx2")),
    am.Event(3390, lambda c: c.set_data(
        "history", [], "refresh", True
    )),

    am.Event(3390, lambda c: c.set_generator_data(
        "fundingx2", 0,
        "text", data_strings["fundingx2_0"]
    )),

    am.Event(3390, lambda c: c.set_generator_data(
        "fundingx2", 1,
        "text", data_strings["fundingx2_1"]
    )),

    am.Event(3390, lambda c: c.set_generator_data(
        "fundingx2", 3,
        "text", data_strings["fundingx2_2"]
    )),

    am.Event(3895, am.Event.remove_scene("fundingx2")),
    am.Event(3895, am.Event.swap_scene("clear")),
    am.Event(3896, am.Event.swap_scene("ocean_c")),
    *ocean2_events,

    am.Event(4460, am.Event.swap_scene("accesspoints")),
    am.Event(4460, am.Event.layer_scene("fdg_single")),
    am.Event(4534, lambda c: c.set_generator_data(
        "fdg_single", 1, "text", data_strings["fdg_single_0"]
    )),

    am.Event(5500, am.Event.remove_scene("fdg_single")),
    am.Event(5500, am.Event.swap_scene("clear")),
    am.Event(5500, am.Event.swap_scene("beats")),
    am.Event(5500, am.Event.layer_scene("fdg_down")),
    am.Event(5788, lambda c: c.set_generator_data(
        "fdg_down", 0, "text", data_strings["fdg_down_0"]
    )),

    am.Event(5916, lambda c: c.set_generator_data(
        "fdg_down", 0,
        "text", data_strings["fdg_down_1"], "lineno", 0, "offset", 0
    )),

    am.Event(5916, lambda c: c.set_generator_data(
        "fdg_down", 1,
        "text", data_strings["fdg_down_2"]
    )),

    am.Event(6270, am.Event.swap_scene("beats_lr")),

    am.Event(6508, am.Event.remove_scene("fdg_down")),
    # am.Event(6508, am.Event.remove_scene("debug_counter")),

    am.Event(6508, am.Event.swap_scene("clear"))
))


# class MixerWrapper:
#     def __init__(self):
#         self.is_paused = False
#
#     def toggle_music(self):
#         if self.is_paused:
#             pygame.mixer.music.unpause()
#             self.is_paused = False
#         else:
#             pygame.mixer.music.pause()
#             self.is_paused = True
#
#
# ffwing = MixerWrapper()

paused_this_frame = False
ff_this_frame = False

filename = "media/credits.wav"

playback = Playback()
playback.load_file(filename)

print("\033[1;1Hskips\n\n1 | start\n2 | title\n3 | funding\n4 | loading\n5 | break\n6 | final")

# Skips forward to the title scene
time_menu = time.time()
while time.time() - 2 < time_menu:
    if keyboard.is_pressed("1"):
        time_menu = 99999999999999999999
        break
    elif keyboard.is_pressed("2"):
        skip_beats(controller, 1000, 1081)
        time_menu = 99999999999999999999
        break
    elif keyboard.is_pressed("3"):
        skip_beats(controller, 1770, 1851)
        controller.events[1849] = am.Event(1849, am.Event.layer_scene("redraw_ui")),
        controller.events[1860] = am.Event(1860, am.Event.remove_scene("redraw_ui")),
        time_menu = 99999999999999999999
        break
    elif keyboard.is_pressed("4"):
        skip_beats(controller, 3040, 3133)
        time_menu = 99999999999999999999
        break
    elif keyboard.is_pressed("5"):
        skip_beats(controller, 3780, 3898)
        time_menu = 99999999999999999999
        break
    elif keyboard.is_pressed("6"):
        skip_beats(controller, 5420, 5501)
        time_menu = 99999999999999999999
        break

    time.sleep(0.01)


if os.name == "nt":
    os.system("cls")
elif os.name == "posix":
    os.system("clear")
else:
    print("\033[2J")

# wave_obj = sa.WaveObject.from_wave_file(filename)
# play_obj = wave_obj.play()
playback.play()
playback.seek(skip_by)

time_start = time.time()
last_update = time.time()
prev_pos = 0

while playback.active:
    # (17.06.21) might have broken, i used a -1 beat offset here to try and sync up everything better
    # since i originally used 1-indexed beats
    #
    # (24.06.21) update chat it didnt break

    # next_beat = (time.time() - time_start - offset) > ((beat - 1) * delay)
    next_beat = (playback.curr_pos - offset) > ((beat - 1) * delay)
    need_update = time.time() - (1/30) > last_update
    # print(pygame.mixer.music.get_pos())

    if next_beat:
        controller.request_next()
        canvas.render_all()
        last_frames.append(time.time())
        if len(last_frames) > 10:
            last_frames.pop(0)

        beat += 1

    if need_update:
        if keyboard.is_pressed("p"):
            if not paused_this_frame:
                if playback.paused:
                    playback.resume()
                else:
                    playback.pause()

                paused_this_frame = True
        else:
            paused_this_frame = False

        if keyboard.is_pressed(","):
            if not ff_this_frame:
                ff_this_frame = True
            else:
                playback.seek(playback.curr_pos + delay * 3)

        if keyboard.is_pressed("."):
            if not ff_this_frame:
                ff_this_frame = True
            else:
                playback.seek(playback.curr_pos + delay * 7)

        if keyboard.is_pressed("/"):
            if not ff_this_frame:
                ff_this_frame = True
            else:
                playback.seek(playback.curr_pos + delay * 15)
        # else:
        #     # print("n", ff_this_frame, pygame.mixer.music.get_pos() + prev_pos, prev_pos)
        #     if ff_this_frame:
        #         # print("unpausing now")
        #         ff_this_frame = False
        #         ffwing.toggle_music()

        last_update = time.time()
