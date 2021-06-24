# adapted from the-sea.js by plaao (me)

# The ocean is stored as a list of strings which is combined into one string when rendered.
# It is rendered internally in 40x8 resolution.
import math
import random

ocean_time = math.floor(random.random() * 2000)
alphabet = "abcdefghijklmnopqrstuvwxyz"


def init_populate_ocean():
    global ocean_time

    # Create 12 lists of 80 chars each and get an ocean slice for every ocean time value needed.
    ocean_base = get_ocean_slices(ocean_time, ocean_time + 80)

    ocean_time += 80
    return ocean_base


def get_ocean_slice(xr, glitch):
    x = xr / 5
    c = math.cos(0.2 * x) + math.sin(0.3 * x) * math.sin(0.23 * x)
    y = -math.floor(2 * c * math.sin(x)) + 3

    # Returns a list of chars which can then be populated into the ocean.
    cont_list = []
    for i in range(10):
        if random.random() <= 0.002 * glitch:
            cont_list.append(alphabet[math.floor(random.random() * len(alphabet))])

        else:
            if i == y:
                cont_list.append("#")
            elif i > y:
                cont_list.append(".")
            else:
                cont_list.append(" ")

    return cont_list


def mutate_text(txt, glitch):
    for i in range(len(txt)):
        ch = txt[i]
        if ch in "#. " and random.random() <= (0.0002 + ((ocean_time % 1200) / 1200000)) * glitch:
            txt = txt[:i] + alphabet[math.floor(random.random() * len(alphabet))] + txt[i + 1:]

    return txt


def get_ocean_slices(x1, x2):
    cont_list = [
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        ""
    ]

    for xr in range(x1, x2):
        x = xr / 5
        c = math.cos(0.2 * x) + math.sin(0.3 * x) * math.sin(0.23 * x)
        y = -math.floor(2 * c * math.sin(x)) + 3

        # Returns a list of chars which can then be populated into the ocean.
        for i in range(10):
            if random.random() <= 0.002:
                cont_list[i] += alphabet[math.floor(random.random() * len(alphabet))]

            else:
                if i == y:
                    cont_list[i] += "#"
                elif i > y:
                    cont_list[i] += "."
                else:
                    cont_list[i] += " "

    return cont_list


def update_ocean_slices(ocean_content, ocean_glitch):
    global ocean_time
    
    # edits in place
    # get the new slice
    ocean_slice = get_ocean_slice(ocean_time, ocean_glitch)
    ocean_time += 1
    
    # for every line in content, remove the first char and add the slice char
    for i in range(10):
        ocean_content[i] = ocean_content[i][1:] + ocean_slice[i]

    raw_txt = unpack_content_to_text(ocean_content)
    
    return mutate_text(raw_txt, ocean_glitch)


def unpack_content_to_text(content):
    # Join every line with \n
    return "".join(line for line in content)


def begin_ocean():
    return init_populate_ocean()
