# Contains functions used inside credits.py.
# Reduce clutter. Reuse clutter. Recycle clutter.
import random
from CLIRender.dat import Vector2
from colorama import Fore, Style


def generate_random_hex(length):
    return ('%0' + str(length) + 'x') % random.randrange(16 ** length)


def replace_text_with_spaces(string, chance):
    return "".join((" " if random.randint(0, 100) < chance else char) for char in string)


def render_weather(c, layer, x, y, weather, mutations_after=0, spc_chance=0):
    # .                      .
    if weather.precip != -1:
        c.set_string(
            layer, Vector2(x + 5, y - 2),
            replace_text_with_spaces("{:>14}".format(weather.weather_name), spc_chance),
            Fore.YELLOW + Style.NORMAL
        )
    else:
        c.set_string(
            layer, Vector2(x, y - 2),
            replace_text_with_spaces("{:>14}".format(weather.weather_name), spc_chance),
            Fore.RED + Style.BRIGHT
        )

    temp_colour = (Fore.WHITE, Fore.CYAN, Fore.YELLOW, Fore.RED)[min(3, int(weather.temp) // 23)]
    c.set_string(
        layer, Vector2(x, y),
        replace_text_with_spaces("{:2}°F  ".format(int(weather.temp)), spc_chance),
        temp_colour + Style.BRIGHT
    )

    wind_dirs = ("N ", "NE", "E ", "SE", "S ", "SW", "W ", "NW")
    c.set_string(
        layer, Vector2(x + 5, y),
        replace_text_with_spaces("Wind {:2} mph {}".format(int(weather.wind), wind_dirs[weather.wind_dir]), spc_chance),
        Fore.CYAN + Style.BRIGHT
    )

    c.set_string(
        layer, Vector2(x + 5, y + 2),
        replace_text_with_spaces("Precipitation ", spc_chance),
        Fore.BLUE + Style.BRIGHT
    )

    c.set_string(
        layer, Vector2(x + 5, y + 3),
        replace_text_with_spaces("{:^13} ".format(str(round(weather.precip * 100, 2)) + "%"), spc_chance),
        Fore.BLUE + Style.BRIGHT
    )

    weather.mutate(mutations_after)


def noise(c, layer, amount, chars, colours):
    for n in range(amount):
        location = Vector2(random.randint(0, c.dimensions.x - 1), random.randint(0, c.dimensions.y - 1))
        c.set_char(
            layer, location, random.choice(chars), random.choice(colours)
        )


def set_multiline_string(c, layer, x, y, string, col):
    for offset, line in enumerate(string.split("\n")):
        c.set_string(
            layer, Vector2(x, y + offset), line, col
        ),


def type_text(c, generator, layer, x, y, col, render=True):
    # pop a char off the manager's text if there is one
    text_get = generator.get_data("text")
    offset = generator.get_data("offset")
    total_chars = 0
    add_offset = 0
    if text_get:
        if text_get.startswith("[##CLEAR|"):
            clear_bounds = text_get.split("|")[1].split(";")
            for yclear in range(int(clear_bounds[1])):
                location = Vector2(x, y + yclear)

                if render:
                    c.set_string(
                        layer, location, " " * int(clear_bounds[0]), col
                    )
        else:
            for linecount, text_line in enumerate(text_get.split("\n")):
                local_offset = offset - total_chars
                if 0 <= local_offset < len(text_get):
                    place_typer = local_offset < len(text_line) - 1
                    string = text_line[:local_offset] + ("_" if place_typer else "")
                    if local_offset < len(text_line) and text_line[local_offset] == "@":
                        add_offset += 3

                    string = string.replace("~", "").replace("@", "")
                    total_chars += len(text_line)
                    location = Vector2(x, y + linecount)

                    if render:
                        c.set_string(
                            layer, location, string, col
                        )

            generator.oper_data("offset", lambda t: t + 1 + add_offset)


def fuck_up_text(string, chance, also_ignore=""):
    new_str = ""
    fucks = (
        ".", ".", ".", " ", " ", "`", "=", "/", "?", "-", "$", "%"
    )
    for char in string:
        if char == "\n":
            new_str += char
        else:
            if random.randint(1, 1000) < chance and char not in "@~\n" + also_ignore:
                new_str += random.choice(fucks)
            else:
                new_str += char

    return new_str


def debug_info(c, g, b, frames):
    c.set_string(
        0, Vector2(32, 1), "{:4} g | {:4} l".format(g.parent.cur_beat, g.parent.active_scene[0].internal_beat), Style.BRIGHT + Fore.YELLOW
    ),
    counted_scenes = 0
    for index, scene in enumerate(filter(lambda s: s.name != "debug_counter", g.parent.active_scene)):
        c.set_string(
            0, Vector2(32, index + 2), "{:^17}".format(
                scene.name + " ({})".format(len(list(filter(lambda g: g.start_beat <= b, scene.generators))))
            ), Style.NORMAL + Fore.GREEN
        ),

        counted_scenes += 1

    for index2 in range(counted_scenes, 6):
        c.set_string(
            0, Vector2(32, index2 + 2), "                 ", Style.NORMAL + Fore.GREEN
        ),

    c.set_string(
        0, Vector2(32, 8), "  {:4} e/s".format(c.edits_this_frame), Style.BRIGHT + Fore.YELLOW
    ),

    avg_differences = sum(frames[i] - frames[i - 1] for i in range(len(frames) - 1, 0, -1))
    if avg_differences:
        avg_differences /= 10
    else:
        avg_differences = 60

    c.set_string(
        0, Vector2(32, 9), " {:6} fps".format(round(1 / avg_differences, 1)), Style.BRIGHT + Fore.YELLOW
    ),

    cols = (
        Fore.BLACK,
        Fore.RED,
        Fore.GREEN,
        Fore.YELLOW,
        Fore.BLUE,
        Fore.MAGENTA,
        Fore.CYAN,
        Fore.WHITE,
    )

    styles = (
        Style.NORMAL,
        Style.BRIGHT
    )
    for index in range(16):
        c.set_char(
            0, Vector2(32 + (index % 8), 11 + (index // 8)), "##", cols[index % 8] + styles[index // 8]
        ),


def clear(c, layer):
    c.clear_layer(layer)


def beat_toggle(c, g, layer, x, x2, y, y2, char, col):
    tog = g.get_data("beat_toggle")
    chars = char if tog else ".."
    x_diff = x2 - x
    for yn in range(y, y2):
        c.set_string(
            layer, Vector2(x, yn), chars * x_diff, col
        ),

    g.set_data("beat_toggle", not tog)


def work_out_date(b, day_offset=0):
    # "22.10.2009"
    lengths = (
        31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
    )

    # One day passes every 64 beats.
    days_needed = (b // 64) + day_offset

    month_loc = 9
    day_loc = 22
    year = 2009
    while days_needed > 0:
        leap_year = (1 if year % 4 == 0 and month_loc == 1 else 0)  # leap year
        until_end_month = lengths[month_loc] + 1 - day_loc + leap_year
        day_loc += min(days_needed, until_end_month)
        days_needed -= min(days_needed, until_end_month)

        if day_loc > lengths[month_loc] + leap_year:
            month_loc += 1
            day_loc = 1
            if month_loc >= 12:
                month_loc = 0
                year += 1

    return "{:02}.{:02}.{:04}".format(day_loc, month_loc + 1, year)


def split_word_template(string):
    return [sp.split("#") for sp in string.split("\n")]


def typewrite_by_word(c, generator, layer, x, y, col, render=True, history_var="history"):
    # Show the text up to offset words at line lineno
    text_get = generator.get_data("text")
    offset = generator.get_data("offset")
    lineno = generator.get_data("lineno")
    if text_get:
        if lineno < len(text_get):
            line_get = text_get[lineno]
            line_total = "".join(line for line in line_get[:offset])

            if line_get:
                if line_get[0].startswith("[~~CLEAR|"):
                    clear_bounds = line_get[0].split("|")[1]
                    location = Vector2(x, y)

                    if render:
                        c.set_string(
                            layer, location, " " * int(clear_bounds), col
                        )
                else:
                    # print line_total and increment offset by 1.
                    # if offset is > lineno, reset offset and increment lineno
                    # if line_total is empty (offset == 0), print a clear
                    if render:
                        if line_total:
                            c.set_string(
                                layer, Vector2(x, y), line_total.replace("~", ""), col
                            ),
                        else:
                            c.set_string(
                                layer, Vector2(x, y), " " * 60, col
                            ),

                    if offset >= len(line_get):
                        history = generator.parent.get_data(history_var)
                        is_fluff = line_total.startswith(" ") or not line_total
                        is_important = line_total.endswith("~")
                        colour_select = Fore.YELLOW + Style.NORMAL
                        prefix = "- "
                        if is_fluff:
                            prefix = "  "
                            colour_select = Fore.BLACK + Style.BRIGHT
                        elif is_important:
                            prefix = "> "
                            colour_select = Fore.GREEN + Style.NORMAL

                        if not history:
                            history = [(
                                prefix + line_total.strip(" ").replace("~", ""), colour_select
                            )]
                            generator.parent.set_data(history_var, history)
                        else:
                            history.append((
                                prefix + line_total.strip(" ").replace("~", ""), colour_select
                            ))

                        generator.parent.set_data("refresh", True)

                        generator.set_data("offset", 0)
                        generator.set_data("lineno", lineno + 1)
                    else:
                        generator.set_data("offset", offset + 1)

            else:
                generator.set_data("offset", offset + 1)


def write_history(c, generator, layer, x, y, col, stop, var="history"):
    # Write history from y position going upwards until 0
    history = generator.parent.get_data(var)
    need_refresh = generator.parent.get_data("refresh")

    if need_refresh:
        generator.parent.set_data("refresh", False)

        if history:
            lineid = 0
            for ypos in range(y, stop - 1, -1):
                line = history[len(history) - 1 - lineid] if lineid < len(history) else ("", Fore.BLACK + Style.BRIGHT)
                lineid += 1

                location = Vector2(x, ypos)

                c.set_string(
                    layer, location, "{:50}".format(line[0]), line[1]
                ),
        else:
            for ypos in range(y, stop - 1, -1):
                c.set_string(
                    layer, Vector2(x, ypos), " " * 50, Fore.BLACK + Style.NORMAL
                ),


def show_access_point_visual(c, generator, layer, x, y):
    # Increment counter. If counter > 8, reset it, increment the bigger counter
    counter = generator.get_data("counter")
    block_counter = generator.get_data("block")
    location_x = 5 * (block_counter % 6) + x
    location_y = 4 * (block_counter // 6) + y

    if counter < 8:
        set_multiline_string(
            c, layer, location_x, location_y,
            "  ###  \nPBS #{:02}\nPing  {}".format(block_counter + 1, counter + 1), Fore.YELLOW + Style.NORMAL
        )

        generator.oper_data("counter", lambda t: t + 1)
    else:
        set_multiline_string(
            c, layer, location_x, location_y,
            "  ...  \nPBS #{:02}\n-------".format(block_counter + 1), Fore.BLACK + Style.BRIGHT
        )

        location_x_next = 5 * ((block_counter + 1) % 6) + x
        location_y_next = 4 * ((block_counter + 1) // 6) + y

        set_multiline_string(
            c, layer, location_x_next, location_y_next,
            "  ###  \nPBS #{:02}\nPing  {}".format(block_counter + 2, 1), Fore.YELLOW + Style.NORMAL
        )

        generator.set_data("counter", 1)
        generator.oper_data("block", lambda t: t + 1)


def make_poweroff_bars(c, b, layer, col):
    # at b=1, full screen
    # then lerp height on both ends down to 0
    height = int(24 / (b ** 1.3))
    location = Vector2(0, 12 - (height // 2))

    c.set_string(
        layer, location, ("##" * 40) * height, col
    )