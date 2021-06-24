# Contains all animation scenes except for debug_counter.
# Use variable "all_scenes" which contains all scenes defined here.
# This file also creates the canvas.

import animator as am
from animation_functions import *
from animation_classes import known_weathers
from ocean import begin_ocean, update_ocean_slices
from CLIRender.classes import Canvas

canvas = Canvas(Vector2(40, 24), 1, ())

wipe = am.Scene(
    "wipe",
    (
        am.Generator(
            0, am.Generator.always(),
            am.Generator.no_create(),
            lambda g, b: noise(
                canvas, 0, int(b ** 1.4), ("##", "@@", "  "),
                (
                    *((Style.BRIGHT + Fore.WHITE,) * b),
                    *((Style.NORMAL + Fore.WHITE,) * (70 - b)),
                    *((Style.BRIGHT + Fore.BLACK,) * 4 * (40 - b)),
                )
            ),
            am.Generator.no_request()
        ),
    )
)


clear_wipe = am.Scene(
    "clear_wipe",
    (
        am.Generator(
            0, am.Generator.always(),
            am.Generator.no_create(),
            lambda g, b: noise(
                canvas, 0, int(b ** 2.2), ("  ",), (Fore.WHITE + Style.BRIGHT,)
            ),
            am.Generator.no_request()
        ),
    )
)


clear_scene = am.Scene(
    "clear",
    (
        am.Generator(
            0, am.Generator.at_beat(0),
            lambda g: noise(
                canvas, 0, 40 * 24, ("##",), (Style.BRIGHT + Fore.WHITE,)
            ),
            am.Generator.no_request(), am.Generator.no_request()
        ),

        am.Generator(
            1, am.Generator.always(),
            lambda g: clear(canvas, 0),
            am.Generator.no_request(), am.Generator.no_request()
        ),
    )
)


ocean = am.Scene(
    "ocean_b",
    (
        am.Generator(
            0, am.Generator.every_n_beats(2),
            lambda g: g.set_data("ocean", begin_ocean(), "ocean_glitch", 1, "ocean_col", Style.BRIGHT + Fore.BLUE),
            lambda g, b: canvas.set_string(
                0, Vector2(0, 14), update_ocean_slices(g.get_data("ocean"),
                                                       g.get_data("ocean_glitch")), g.get_data("ocean_col")
            ),
            am.Generator.no_request()
        ),

        am.Generator(
            0, am.Generator.always(),
            lambda g: g.set_data("text", "", "offset", 0),
            lambda g, b: type_text(canvas, g, 0, 1, 1, Style.BRIGHT + Fore.WHITE),
            am.Generator.no_request()
        ),
    )
)


ocean2 = am.Scene(
    "ocean_c",
    (
        am.Generator(
            0, am.Generator.every_n_beats(2),
            lambda g: g.set_data("ocean", begin_ocean(), "ocean_glitch", 16, "ocean_col", Style.BRIGHT + Fore.BLACK),
            lambda g, b: canvas.set_string(
                0, Vector2(0, 14), update_ocean_slices(g.get_data("ocean"),
                                                       g.get_data("ocean_glitch")), g.get_data("ocean_col")
            ),
            am.Generator.no_request()
        ),

        am.Generator(
            0, am.Generator.always(),
            lambda g: g.set_data("text", "", "offset", 0),
            lambda g, b: type_text(canvas, g, 0, 1, 1, Style.BRIGHT + Fore.RED, int(b ** 1.143) % 20 not in (0, 8, 17, 15)),
            am.Generator.no_request()
        ),

        am.Generator(
            0, am.Generator.always(),
            lambda g: g.set_data("text", "", "offset", 0),
            lambda g, b: type_text(canvas, g, 0, 1, 1, Style.BRIGHT + Fore.RED, int(b ** 1.2) % 20 in (0, 15)),
            am.Generator.no_request()
        ),

        am.Generator(
            0, am.Generator.always(),
            lambda g: g.set_data("text", "", "offset", 0),
            lambda g, b: type_text(canvas, g, 0, 1, 1, Style.BRIGHT + Fore.RED, int(b ** 1.2) % 20 == 8),
            am.Generator.no_request()
        ),

        am.Generator(
            0, am.Generator.always(),
            lambda g: g.set_data("text", "", "offset", 0),
            lambda g, b: type_text(canvas, g, 0, 1, 1, Style.BRIGHT + Fore.RED, int(b ** 1.2) % 20 == 17),
            am.Generator.no_request()
        ),
    )
)


ocean3 = am.Scene(
    "ocean_d",
    (
        am.Generator(
            0, am.Generator.always(),
            lambda g: g.set_data("ocean", begin_ocean(), "ocean_glitch", 100, "ocean_col", Style.NORMAL + Fore.MAGENTA),
            lambda g, b: canvas.set_string(
                0, Vector2(0, 14), update_ocean_slices(g.get_data("ocean"),
                                                       g.get_data("ocean_glitch")), g.get_data("ocean_col")
            ),
            am.Generator.no_request()
        ),

        am.Generator(
            0, am.Generator.always(),
            am.Generator.no_create(),
            lambda g, b: set_multiline_string(canvas, 0, 1, 1,
                                              "The system has encountered a fatal error. Please wait.\n\n"
                                              "[ERR: 801]\n\n" + "\n".join(
                                                  " ".join(generate_random_hex(4) for _ in range(8)) for _ in range(4)
                                              ),
                                              Style.BRIGHT + Fore.RED),
            am.Generator.no_request()
        ),
    )
)


text = am.Scene(
    "typewrite",
    (
        am.Generator(
            0, am.Generator.always(),
            lambda g: g.set_data("text", "", "offset", 0),
            lambda g, b: type_text(canvas, g, 0, 1, 1, Style.BRIGHT + Fore.WHITE),
            am.Generator.no_request()
        ),
    )
)


title = am.Scene(
    "title",
    (
        # We have 12 beat-ends to map to:
        # '  - plaaosert
        # '  - frums
        # '  - python 3.6
        # '  - command line
        # drums
        # '  -
        # '  -
        # '  -
        # '  -
        # small moog
        # '  -
        # '  -
        # '  -
        # '  -

        am.Generator(
            64, am.Generator.at_beat(64),
            am.Generator.no_create(),
            lambda g, b: canvas.set_string(
                0, Vector2(1, 1), "animation | plaaosert", Fore.CYAN + Style.BRIGHT
            ),
            am.Generator.no_request()
        ),

        am.Generator(
            128, am.Generator.at_beat(128),
            am.Generator.no_create(),
            lambda g, b: canvas.set_string(
                0, Vector2(1, 2), "bgm       | Frums - Credits", Fore.CYAN + Style.BRIGHT
            ),
            am.Generator.no_request()
        ),

        am.Generator(
            192, am.Generator.at_beat(192),
            am.Generator.no_create(),
            lambda g, b: canvas.set_string(
                0, Vector2(1, 4), "running pure Python 3.6", Fore.CYAN + Style.NORMAL
            ),
            am.Generator.no_request()
        ),

        am.Generator(
            256, am.Generator.at_beat(256),
            am.Generator.no_create(),
            lambda g, b: canvas.set_string(
                0, Vector2(1, 5), "in the command line", Fore.CYAN + Style.NORMAL
            ),
            am.Generator.no_request()
        ),

        am.Generator(
            320, am.Generator.at_beat(320),
            am.Generator.no_create(),
            lambda g, b: canvas.set_string(
                0, Vector2(0, 21), "--" * 40, Fore.WHITE + Style.BRIGHT
            ),
            am.Generator.no_request()
        ),

        am.Generator(
            384, am.Generator.at_beat(384),
            am.Generator.no_create(),
            lambda g, b: canvas.set_string(
                0, Vector2(1, 22), "> _ ", Fore.WHITE + Style.BRIGHT
            ),
            am.Generator.no_request()
        ),

        am.Generator(
            448, am.Generator.at_beat(448),
            am.Generator.no_create(),
            lambda g, b: set_multiline_string(
                canvas, 0, 26, 14, "----------------------------\n" +
                                   "|                          |\n" * 6, Fore.WHITE + Style.BRIGHT
            ),
            am.Generator.no_request()
        ),

        am.Generator(
            512, am.Generator.at_beat(512),
            am.Generator.no_create(),
            lambda g, b: set_multiline_string(
                canvas, 0, 27, 15, "22.10.2009", Fore.YELLOW + Style.BRIGHT
            ),
            am.Generator.no_request()
        ),

        am.Generator(
            576, am.Generator.at_beat(576),
            am.Generator.no_create(),
            lambda g, b: set_multiline_string(
                canvas, 0, 26, 16, "----------------------------", Fore.WHITE + Style.BRIGHT
            ),
            am.Generator.no_request()
        ),

        am.Generator(
            640, am.Generator.at_beat(640),
            am.Generator.no_create(),
            lambda g, b: set_multiline_string(
                canvas, 0, 27, 17, "43°F      Wind 13 mph W \n"
                                   "                        ", Fore.CYAN + Style.BRIGHT
            ),
            am.Generator.no_request()
        ),

        am.Generator(
            704, am.Generator.at_beat(704),
            am.Generator.no_create(),
            lambda g, b: set_multiline_string(
                canvas, 0, 32, 19, "Precipitation \n"
                                   "    20.3%     ", Fore.BLUE + Style.BRIGHT
            ),
            am.Generator.no_request()
        ),

        am.Generator(
            768, am.Generator.at_beat(768),
            am.Generator.no_create(),
            lambda g, b: set_multiline_string(
                canvas, 0, 36, 15, "Cloudy", Fore.YELLOW + Style.NORMAL
            ),
            am.Generator.no_request()
        ),
    )
)


beats = am.Scene(
    "beats",
    (
        # beat manager
        am.Generator(
            0, am.Generator.combine_conditions(am.Generator.every_on_off(48, 16), am.Generator.every_n_beats(4)),
            lambda g: g.set_data("beat_toggle", True),
            lambda g, b: beat_toggle(canvas, g, 0, 18, 22, 11, 15, "@@", Style.BRIGHT + Fore.YELLOW),
            am.Generator.no_request()
        ),
        am.Generator(
            0, am.Generator.combine_conditions(am.Generator.every_off_on(48, 16), am.Generator.every_n_beats(2)),
            lambda g: g.set_data("beat_toggle", True),
            lambda g, b: beat_toggle(canvas, g, 0, 18, 22, 11, 15, "##", Style.BRIGHT + Fore.GREEN),
            am.Generator.no_request()
        ),
    )
)

beats_lr = am.Scene(
    "beats_lr",
    (
        # beat manager
        am.Generator(
            0, am.Generator.combine_conditions(am.Generator.every_on_off(48, 16), am.Generator.every_n_beats(4)),
            lambda g: g.set_data("beat_toggle", True),
            lambda g, b: beat_toggle(canvas, g, 0, 18, 20, 11, 15, "@@", Style.BRIGHT + Fore.YELLOW),
            am.Generator.no_request()
        ),
        am.Generator(
            0, am.Generator.combine_conditions(am.Generator.every_off_on(48, 16), am.Generator.every_n_beats(2)),
            lambda g: g.set_data("beat_toggle", True),
            lambda g, b: beat_toggle(canvas, g, 0, 20, 22, 11, 15, "##", Style.BRIGHT + Fore.GREEN),
            am.Generator.no_request()
        ),
    )
)


beats_side = am.Scene(
    "beats_side",
    (
        # beat manager
        am.Generator(
            0, am.Generator.combine_conditions(am.Generator.every_on_off(48, 16), am.Generator.every_n_beats(4)),
            lambda g: g.set_data("beat_toggle", True),
            lambda g, b: beat_toggle(canvas, g, 0, 18, 20, 11, 15, "@@", Style.BRIGHT + Fore.YELLOW),
            am.Generator.no_request()
        ),
        am.Generator(
            0, am.Generator.combine_conditions(am.Generator.every_off_on(48, 16), am.Generator.every_n_beats(2)),
            lambda g: g.set_data("beat_toggle", True),
            lambda g, b: beat_toggle(canvas, g, 0, 20, 22, 11, 15, "##", Style.BRIGHT + Fore.GREEN),
            am.Generator.no_request()
        ),
    )
)


date_ticker = am.Scene(
    "dates",
    (
        # TODO change this shit to every n beats, use a data variable to store the current date index PLEASE
        #
        # Run at normal speed
        # Run at double speed
        # Run with slight randomness forwards
        # Skip forwards, go every step
        # At crazy part, switch off this and go to a glitchy display
        #
        am.Generator(
            0, am.Generator.before_n(64 * 8),
            am.Generator.no_create(),
            lambda g, b: canvas.set_string(
                0, Vector2(27, 15), work_out_date(b), Fore.YELLOW + Style.BRIGHT
            ),
            am.Generator.no_request()
        ),

        am.Generator(
            64 * 8, am.Generator.before_n(64 * 12 - 4),
            am.Generator.no_create(),
            lambda g, b: canvas.set_string(
                0, Vector2(27, 15), work_out_date((64 * 8) + (b - (64 * 8)) * 2), Fore.YELLOW + Style.BRIGHT
            ),
            am.Generator.no_request()
        ),

        am.Generator(
            64 * 12 - 4, am.Generator.at_beat(64 * 12 - 4),
            am.Generator.no_create(),
            lambda g, b: canvas.set_string(
                0, Vector2(27, 15), "??.??.????", Fore.YELLOW + Style.BRIGHT
            ),
            am.Generator.no_request()
        ),

        am.Generator(
            64 * 12 + 4, am.Generator.combine_conditions(am.Generator.every_n_beats(4), am.Generator.before_n(64 * 16)),
            am.Generator.no_create(),
            lambda g, b: canvas.set_string(
                0, Vector2(27, 15), work_out_date(random.randint(64 * 12 + b * 8, 64 * 12 + b * 24)), Fore.YELLOW + Style.BRIGHT
            ),
            am.Generator.no_request()
        ),

        am.Generator(
            64 * 16, am.Generator.always(),
            am.Generator.no_create(),
            lambda g, b: canvas.set_string(
                0, Vector2(27, 15), work_out_date(64 * 16 + b * 64 - 64 * 16 * 32), Fore.YELLOW + Style.BRIGHT
            ),
            am.Generator.no_request()
        ),
    )
)


redraw_ui = am.Scene(
    "redraw_ui",
    (
        am.Generator(
            0, am.Generator.at_beat(0),
            am.Generator.no_create(),
            lambda g, b: canvas.set_string(
                0, Vector2(0, 21), "--" * 40, Fore.WHITE + Style.BRIGHT
            ),
            am.Generator.no_request()
        ),

        am.Generator(
            0, am.Generator.at_beat(0),
            am.Generator.no_create(),
            lambda g, b: canvas.set_string(
                0, Vector2(1, 22), "> _ ", Fore.WHITE + Style.BRIGHT
            ),
            am.Generator.no_request()
        ),

        am.Generator(
            0, am.Generator.at_beat(2),
            am.Generator.no_create(),
            lambda g, b: set_multiline_string(
                canvas, 0, 26, 14, "----------------------------\n" +
                                   "|                          |\n" * 6, Fore.WHITE + Style.BRIGHT
            ),
            am.Generator.no_request()
        ),

        am.Generator(
            0, am.Generator.at_beat(3),
            am.Generator.no_create(),
            lambda g, b: set_multiline_string(
                canvas, 0, 27, 15, "22.10.2009", Fore.YELLOW + Style.BRIGHT
            ),
            am.Generator.no_request()
        ),

        am.Generator(
            0, am.Generator.at_beat(4),
            am.Generator.no_create(),
            lambda g, b: set_multiline_string(
                canvas, 0, 26, 16, "----------------------------", Fore.WHITE + Style.BRIGHT
            ),
            am.Generator.no_request()
        ),

        am.Generator(
            0, am.Generator.at_beat(5),
            am.Generator.no_create(),
            lambda g, b: set_multiline_string(
                canvas, 0, 27, 17, "43°F      Wind 13 mph W ", Fore.CYAN + Style.BRIGHT
            ),
            am.Generator.no_request()
        ),

        am.Generator(
            0, am.Generator.at_beat(6),
            am.Generator.no_create(),
            lambda g, b: set_multiline_string(
                canvas, 0, 32, 19, "Precipitation \n"
                                   "    20.3%     ", Fore.BLUE + Style.BRIGHT
            ),
            am.Generator.no_request()
        ),

        am.Generator(
            0, am.Generator.at_beat(7),
            am.Generator.no_create(),
            lambda g, b: set_multiline_string(
                canvas, 0, 36, 15, "Cloudy", Fore.YELLOW + Style.NORMAL
            ),
            am.Generator.no_request()
        ),
    )
)


weather = am.Scene(
    "weather",
    (
        am.Generator(
            0, am.Generator.combine_conditions(am.Generator.every_n_beats(64), am.Generator.before_n(64 * 8)),
            am.Generator.no_create(),
            lambda g, b: render_weather(canvas, 0, 27, 17, known_weathers[min(2, b // 64)], 0 if b < 128 else 1),
            am.Generator.no_request()
        ),
        am.Generator(
            64 * 8, am.Generator.combine_conditions(am.Generator.every_n_beats(32), am.Generator.before_n(64 * 12)),
            am.Generator.no_create(),
            lambda g, b: render_weather(canvas, 0, 27, 17, known_weathers[2], 1),
            am.Generator.no_request()
        ),

        am.Generator(
            64 * 12 - 4, am.Generator.at_beat(64 * 12 - 4),
            am.Generator.no_create(),
            lambda g, b: render_weather(canvas, 0, 27, 17, known_weathers[4], 1),
            am.Generator.no_request()
        ),

        am.Generator(
            64 * 12 + 4, am.Generator.combine_conditions(am.Generator.every_n_beats(4), am.Generator.before_n(64 * 16)),
            am.Generator.no_create(),
            lambda g, b: render_weather(canvas, 0, 27, 17, known_weathers[2], 14),
            am.Generator.no_request()
        ),
        am.Generator(
            64 * 16, am.Generator.always(),
            am.Generator.no_create(),
            lambda g, b: render_weather(canvas, 0, 27, 17, known_weathers[3], 1, max(0, (b - 1080) * 2.2)),
            am.Generator.no_request()
        ),
    )
)


funding = am.Scene(
    "funding",
    (
        am.Generator(
            0, am.Generator.always(),
            lambda g: g.set_data("text", [], "offset", 0, "lineno", 0, "type_col", Fore.WHITE + Style.BRIGHT),
            lambda g, b: typewrite_by_word(canvas, g, 0, 2, 22, g.get_data("type_col")),
            am.Generator.no_request()
        ),

        am.Generator(
            0, am.Generator.always(),
            am.Generator.no_create(),
            lambda g, b: write_history(canvas, g, 0, 1, 19, Fore.BLACK + Style.BRIGHT, 1),
            am.Generator.no_request()
        ),
    )
)


loading = am.Scene(
    "loadingbar",
    (
        am.Generator(
            0, am.Generator.at_beat(0),
            lambda g: g.scene.set_data("progress", 0),
            lambda g, b: set_multiline_string(canvas, 0, 2, 9,
                                              "----------------------------------\n"
                                              "|                                |\n"
                                              "----------------------------------",
                                              Fore.WHITE + Style.BRIGHT),
            am.Generator.no_request()
        ),

        am.Generator(
            1, am.Generator.at_beat(1),
            lambda g: g.scene.set_data("progress", 0),
            lambda g, b: set_multiline_string(canvas, 0, 3, 10,
                                              "          Loading...          \n",
                                              Fore.BLACK + Style.BRIGHT),
            am.Generator.no_request()
        ),

        am.Generator(
            0, am.Generator.combine_conditions(am.Generator.before_n(240), am.Generator.every_n_beats(8)),
            am.Generator.no_create(),
            lambda g, b: g.scene.oper_data("progress", lambda t: t + 1),
            am.Generator.no_request()
        ),

        am.Generator(
            240, am.Generator.always(),
            am.Generator.no_create(),
            lambda g, b: g.scene.oper_data("progress", lambda t: t + random.randint(40, 70)),
            am.Generator.no_request()
        ),

        am.Generator(
            0, am.Generator.before_n(240),
            am.Generator.no_create(),
            lambda g, b: canvas.set_string(0, Vector2(3, 10), "#" * g.scene.get_data("progress"),
                                           Fore.YELLOW + Style.BRIGHT),
            am.Generator.no_request()
        ),

        am.Generator(
            240, am.Generator.always(),
            am.Generator.no_create(),
            lambda g, b: canvas.set_string(0, Vector2(3, 10), fuck_up_text("#" * g.scene.get_data("progress"), 400),
                                           Fore.RED + Style.BRIGHT),
            am.Generator.no_request()
        ),

        am.Generator(
            0, am.Generator.before_n(240),
            lambda g: g.set_data("text", [], "offset", 0, "lineno", 0, "type_col", Fore.BLACK + Style.BRIGHT),
            lambda g, b: typewrite_by_word(canvas, g, 0, 3, 12, g.get_data("type_col")),
            am.Generator.no_request()
        ),
    )
)


quick_loading = am.Scene(
    "fastload",
    (
        am.Generator(
            0, am.Generator.at_beat(0),
            lambda g: g.scene.set_data("progress", 0),
            lambda g, b: set_multiline_string(canvas, 0, 2, 9,
                                              "----------------------------------\n"
                                              "|                                |\n"
                                              "----------------------------------",
                                              Fore.WHITE + Style.BRIGHT),
            am.Generator.no_request()
        ),

        am.Generator(
            1, am.Generator.at_beat(1),
            lambda g: g.scene.set_data("progress", 0),
            lambda g, b: set_multiline_string(canvas, 0, 3, 10,
                                              "        Please wait...        \n",
                                              Fore.BLACK + Style.BRIGHT),
            am.Generator.no_request()
        ),

        am.Generator(
            0, am.Generator.always(),
            am.Generator.no_create(),
            lambda g, b: g.scene.oper_data("progress", lambda t: t + random.randint(4, 6)),
            am.Generator.no_request()
        ),

        am.Generator(
            0, am.Generator.always(),
            am.Generator.no_create(),
            lambda g, b: canvas.set_string(0, Vector2(3, 10), "#" * g.scene.get_data("progress"),
                                           Fore.GREEN + Style.BRIGHT),
            am.Generator.no_request()
        ),
    )
)


error_screen = am.Scene(
    "error",
    (
        am.Generator(
            0, am.Generator.at_beat(0),
            lambda g: g.scene.set_data("progress", 0),
            lambda g, b: set_multiline_string(canvas, 0, 0, 14, "--" * 40 + "\n" * 8 + "  $ ", Fore.WHITE + Style.BRIGHT),
            am.Generator.no_request()
        ),

        am.Generator(
            0, am.Generator.at_beat(0),
            lambda g: g.scene.set_data("progress", 0),
            lambda g, b: set_multiline_string(canvas, 0, 1, 1,
                                              "Automatic diagnosis unsuccessful. Please wait.\n> ",
                                              Fore.BLACK + Style.BRIGHT),
            am.Generator.no_request()
        ),
    )
)


funding_double = am.Scene(
    "fundingx2",
    (
        am.Generator(
            0, am.Generator.always(),
            lambda g: g.set_data("text", [], "offset", 0, "lineno", 0, "type_col", Fore.RED + Style.NORMAL),
            lambda g, b: typewrite_by_word(canvas, g, 0, 2, 2, g.get_data("type_col")),
            am.Generator.no_request()
        ),

        # am.Generator(
        #     0, am.Generator.always(),
        #     am.Generator.no_create(),
        #     lambda g, b: write_history(canvas, g, 0, 1, 19, Fore.BLACK + Style.BRIGHT, 1),
        #     am.Generator.no_request()
        # ),

        am.Generator(
            0, am.Generator.always(),
            lambda g: g.set_data("text", [], "offset", 0, "lineno", 0, "type_col", Fore.CYAN + Style.BRIGHT),
            lambda g, b: typewrite_by_word(canvas, g, 0, 2, 22, g.get_data("type_col"), history_var="history2"),
            am.Generator.no_request()
        ),

        am.Generator(
            0, am.Generator.always(),
            am.Generator.no_create(),
            lambda g, b: write_history(canvas, g, 0, 1, 21, Fore.BLACK + Style.BRIGHT, 15, var="history2"),
            am.Generator.no_request()
        ),

        am.Generator(
            0, am.Generator.always(),
            lambda g: g.set_data("text", [], "offset", 0, "lineno", 0, "type_col", Fore.YELLOW + Style.BRIGHT),
            lambda g, b: typewrite_by_word(canvas, g, 0, 4, 5, g.get_data("type_col"), history_var="history3"),
            am.Generator.no_request()
        ),
    )
)

access_points = am.Scene(
    "accesspoints",
    (
        am.Generator(
            0, am.Generator.combine_conditions(am.Generator.before_n(20), am.Generator.every_n_beats(2)),
            am.Generator.no_create(),
            lambda g, b: set_multiline_string(
                canvas, 0, 1, 1,
                "\n\n".join(
                    "\n".join(
                        "   ".join(
                            ("PBS #{:02}".format((yblock * 6) + x + 1) if yline == 1 else ("  ###  ", "", "Unknown")[yline]) if random.randint(0, max(1, 32 - int(b ** 1.2))) < 4 else "       "
                            for x in range(6)
                        ) for yline in range(3)
                    ) for yblock in range(4)
                ),
                Fore.BLACK + Style.BRIGHT),
            am.Generator.no_request()
        ),

        am.Generator(
            20, am.Generator.at_beat(20),
            am.Generator.no_create(),
            lambda g, b: set_multiline_string(
                canvas, 0, 1, 1,
                "\n\n".join(
                    "\n".join(
                        "   ".join(
                            ("PBS #{:02}".format((yblock * 6) + x + 1) if yline == 1 else ("  ###  ", "", "Unknown")[yline])
                            for x in range(6)
                        ) for yline in range(3)
                    ) for yblock in range(4)
                ),
                Fore.RED + Style.NORMAL),
            am.Generator.no_request()
        ),

        am.Generator(
            0, am.Generator.at_beat(0),
            am.Generator.no_create(),
            lambda g, b: set_multiline_string(canvas, 0, 1, 17,
                                              "No access points are broadcasting.\n"
                                              "Manual search in progress.\n"
                                              "Last search 27.02.2019 (532 days ago)",
                                              Fore.BLACK + Style.BRIGHT),
            am.Generator.no_request()
        ),

        am.Generator(
            80, am.Generator.combine_conditions(am.Generator.every_n_beats(8), am.Generator.before_n(976)),
            lambda g: g.set_data("counter", 0, "block", 0),
            lambda g, b: show_access_point_visual(canvas, g, 0, 1, 1),
            am.Generator.no_request()
        ),

        am.Generator(
            968, am.Generator.at_beat(968),
            am.Generator.no_create(),
            lambda g, b: set_multiline_string(canvas, 0, 6, 9, "  @@@  \nPBS #14\n Active", Fore.GREEN + Style.BRIGHT),
            am.Generator.no_request()
        )
    )
)


funding_single = am.Scene(
    "fdg_single",
    (
        am.Generator(
            0, am.Generator.at_beat(0),
            lambda g: g.scene.set_data("progress", 0),
            lambda g, b: set_multiline_string(canvas, 0, 0, 20, "--" * 40 + "\n" + "  Sending > ",
                                              Fore.WHITE + Style.BRIGHT),
            am.Generator.no_request()
        ),

        am.Generator(
            0, am.Generator.always(),
            lambda g: g.set_data("text", [], "offset", 0, "lineno", 0, "type_col", Fore.YELLOW + Style.NORMAL),
            lambda g, b: typewrite_by_word(canvas, g, 0, 6, 21, g.get_data("type_col")),
            am.Generator.no_request()
        ),
    )
)


funding_down = am.Scene(
    "fdg_down",
    (
        am.Generator(
            0, am.Generator.always(),
            lambda g: g.set_data("text", [], "offset", 0, "lineno", 0, "type_col", Fore.YELLOW + Style.NORMAL),
            lambda g, b: typewrite_by_word(canvas, g, 0, 1, 1 + g.get_data("lineno"), g.get_data("type_col")),
            am.Generator.no_request()
        ),

        am.Generator(
            0, am.Generator.always(),
            lambda g: g.set_data("text", [], "offset", 0, "lineno", 0, "type_col", Fore.YELLOW + Style.NORMAL),
            lambda g, b: typewrite_by_word(canvas, g, 0, 1, 20 + g.get_data("lineno"), g.get_data("type_col")),
            am.Generator.no_request()
        ),
    )
)


poweroff = am.Scene(
    "poweroff",
    (
        am.Generator(
            3, am.Generator.always(),
            am.Generator.no_create(),
            lambda g, b: make_poweroff_bars(canvas, b - 2, 0, Fore.BLACK + Style.NORMAL),
            am.Generator.no_request()
        ),

        am.Generator(
            2, am.Generator.always(),
            am.Generator.no_create(),
            lambda g, b: make_poweroff_bars(canvas, b - 1, 0, Fore.BLACK + Style.BRIGHT),
            am.Generator.no_request()
        ),

        am.Generator(
            1, am.Generator.always(),
            am.Generator.no_create(),
            lambda g, b: make_poweroff_bars(canvas, b, 0, Fore.WHITE + Style.NORMAL),
            am.Generator.no_request()
        ),

        am.Generator(
            0, am.Generator.always(),
            am.Generator.no_create(),
            lambda g, b: make_poweroff_bars(canvas, b + 1, 0, Fore.WHITE + Style.BRIGHT),
            am.Generator.no_request()
        ),
    )
)

all_scenes = (
    wipe, clear_wipe, clear_scene, ocean, ocean2, ocean3, text, title, beats, beats_lr, funding, date_ticker,
    weather, redraw_ui, loading, quick_loading, error_screen, funding_double, access_points, funding_single,
    funding_down, poweroff
)
