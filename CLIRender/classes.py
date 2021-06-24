import os
from platform import system as system_type
from bisect import insort_right, bisect_right

from CLIRender.dat import Vector2


class RenderSection:
    id_inc = 0

    def __init__(self, string, start, code):
        self.id = RenderSection.id_inc
        RenderSection.id_inc += 1

        self.string = string
        self.start = start
        self.length = len(self.string)
        self.end = self.start + self.length
        self.code = code

    def __lt__(self, other):
        return self.start < other

    def __gt__(self, other):
        return self.start > other

    def add_char(self, char):
        self.string += char
        self.end += 2
        self.length += 2

    def mod_char(self, char, loc):
        if loc == self.end:
            self.add_char(char)
        else:
            self.string = self.string[:loc] + char + self.string[loc + 2:]

    # The addition operation adds the other section to this section. The other section takes precedence.
    # This only works with text and discards the other section's code.
    def add_section(self, other):
        diff = other.start - self.start
        self.string = self.string[:diff] + other.string + self.string[diff + other.length:]
        self.length = len(self.string)
        self.start = min(other.start, self.start)
        self.end = self.start + self.length

    # The addition operation adds the other section to this section. The self section takes precedence.
    # This only works with text and discards the other section's code.
    def add_section_below(self, other):
        diff = self.start - other.start
        self.string = other.string[:diff] + self.string + other.string[diff + self.length:]
        self.length = len(self.string)
        self.start = min(other.start, self.start)
        self.end = self.start + self.length

    # Same as section subtraction but only one char.
    def subtract_char(self, loc):
        first = None
        last = None
        if loc > self.start:
            diff = loc - self.start
            first = RenderSection(self.string[:diff], self.start, self.code)

        if loc < self.end:
            diff = self.end - loc
            last = RenderSection(self.string[diff:], loc + 2, self.code)

        return first, last

    # Subtracts another section's length from this section. This returns a 2-tuple containing the two new subsections.
    def subtract_section(self, other):
        first = None
        last = None
        if other.start > self.start:
            # if the other string starts later, there's still a part of the victim string remaining
            diff = other.start - self.start
            first = RenderSection(self.string[:diff], self.start, self.code)

        if other.end < self.end:
            # if the other string ends before us, the latter part needs something too
            diff = self.end - other.end
            last = RenderSection(self.string[self.length - diff:], other.end, self.code)

        return first, last


class Canvas:
    # TODO write multi-layer support. shouldn't be too hard, just merge down layers as we need
    # but not right now. plaao tired

    def __init__(self, dimensions, num_layers, merge_rules):
        self.dimensions = Vector2(dimensions.x * 2, dimensions.y)
        self.num_layers = num_layers
        self.layers = [Layer(i, self.dimensions) for i in range(num_layers)]
        self.merge_rules = merge_rules
        self.edits_this_frame = 0

    def set_char(self, layer, location, char, code):
        self.layers[layer].set_char(int(location.x * 2) + (location.y * self.dimensions.x), char, code)
        self.edits_this_frame += 1

    def set_string(self, layer, location, string, code):
        self.layers[layer].set_string(int(location.x * 2) + (location.y * self.dimensions.x), string, code)
        self.edits_this_frame += 1

    def clear_layer(self, layer):
        self.layers[layer].set_string(0, " " * self.dimensions.x * self.dimensions.y, "")

    def render_blank(self):
        print("\033[1;1H\033[1;37;40m" + (("  " * self.dimensions.x + "\n") * self.dimensions.y))

    def render_all(self):
        # Merge layers from bottom to top then render the resulting group list.
        # Here is the only point we even think about line lengths.
        total_string = "\033[1;1H\033[1;39m"
        for group in self.layers[0].new_groups:
            lineno = group.start // self.dimensions.x
            add_string = ""
            add_string += "\033[{};{}H".format(
                lineno + 1, group.start % self.dimensions.x + 1
            )

            add_string += group.code

            offset = group.start % self.dimensions.x
            # If overrun is greater than x, then it breaks a line boundary.
            # So, for every x overrun, we add a \n between lines.
            split = 0
            stop = 0
            while stop <= group.length:
                if lineno >= self.dimensions.y:
                    break

                stop = self.dimensions.x - offset + split
                add_string += group.string[split:stop] + ("\n" if stop <= group.length else "")
                offset = 0
                lineno += 1
                split += stop - split

            # We're done! How simple ...
            total_string += add_string

        self.layers[0].new_groups.clear()
        self.edits_this_frame = 0
        print(total_string + "\033[27;0H", end="\n")


class Layer:
    def __init__(self, layer_id, dimensions):
        self.dimensions = Vector2(dimensions.x * 2, dimensions.y)
        self.max_loc = self.dimensions.x * self.dimensions.y

        self.id = layer_id
        # new_groups contains a list of groups of text that need to be rendered next time this layer is flattened.
        self.new_groups = []
        self.full_str = ["" for i in range(self.dimensions.x * self.dimensions.y)]

    def set_char(self, loc, char, code):
        # Set a single char in the layer.
        # Step 1: binary search through new_groups to see if we need to make a new group
        # Step 2: make a new group or mod the found group
        #
        # We want to find the rightmost value less than or equal to loc,
        # then check if it encompasses the given position.
        i = bisect_right(self.new_groups, loc) - 1
        if i >= len(self.new_groups) or i < 0:
            i = None
        else:
            # Also check backwards for things with the SAME start location.
            while i >= 1 and self.new_groups[i - 1].start == loc:
                i -= 1

        if i is not None:
            # If a group already exists, we might need to split it.
            # This happens when codes are not equal.
            # In that situation, split our insert group in two and add a new one as normal.
            insert_group = self.new_groups[i]

            # This is only ever relevant when our found group actually reaches loc.
            if insert_group.end >= loc:
                if insert_group.code != code:
                    sub_groups = insert_group.subtract_char(loc)
                    self.new_groups.pop(i)

                    if sub_groups[0]:
                        insort_right(self.new_groups, sub_groups[0])
                    if sub_groups[1]:
                        insort_right(self.new_groups, sub_groups[1])

                    i = None
                else:
                    insert_group.mod_char(char, loc)
            else:
                i = None

        if i is None:
            # Add this char as a new group.
            insort_right(self.new_groups, RenderSection(char, loc, code))

        # Then replace the full string at location with our new thing.
        # This is only as a contingency if our console crashes / burns / explodes / vanishes without a trace.
        # It should be disableable if necessary.

        # print("\n".join("".join(char for char in canvas.layers[0].full_str[line * 40:(line + 1) * 40]) for line in range(10)))
        self.full_str[loc] = code + char

    def has_duplicate_starts(self):
        non_dupe_list = []
        for group in self.new_groups:
            if group in non_dupe_list:
                return False

            non_dupe_list.append(group)

        return True

    def set_string(self, loc, string, code):
        # Find the two groups that are closest to the start and end points of the group.
        # Perform the add function on both if they exist, or the sub function if their code is different.
        # Remove all groups in between.
        # Find the rightmost section with start less than or equal to loc; so, the closest element that can intersect.
        # IT MAY NOT INTERSECT. CHECK. IF IT DOESN'T, THEN NOTHING INTERSECTS START.
        # If we are out of bounds, leave instantly
        if loc >= self.max_loc or loc < 0:
            return

        start_i = bisect_right(self.new_groups, loc) - 1
        if start_i < 0:
            start_i = 0

        # Also check backwards for things with the SAME start location.
        while start_i >= 1 and self.new_groups[start_i - 1].start == loc:
            start_i -= 1

        # Cut the string down to the maximum possible length it could be.
        cut_string = string[:self.max_loc - loc]
        add_group = RenderSection(cut_string, loc, code)
        add_groups = [None, add_group, None]
        remove = []

        for mid_i in range(start_i, len(self.new_groups)):
            # If the group is the same, add. If it's different, subtract.
            # Fill up add_groups with subtracted items.
            mid_group = self.new_groups[mid_i]

            # If it starts after our end, break. We're out.
            if mid_group.start >= add_group.end:
                break

            # If it ends before our start, discard. We don't need it.
            if mid_group.end > add_group.start:
                # If it is eclipsed, we don't need it at all.
                if mid_group.start >= add_group.start and mid_group.end <= add_group.end:
                    remove.append(mid_i)
                else:
                    # Otherwise, run either subtract or add on it.
                    if mid_group.code == add_group.code:
                        # Add the mid group to the code. Delete the mid group.
                        add_group.add_section_below(mid_group)
                        remove.append(mid_i)
                    else:
                        # Subtract the add group from the mid group. Remove previous mid group.
                        sub_groups = mid_group.subtract_section(add_group)
                        if sub_groups[0]:
                            add_groups[0] = sub_groups[0]
                        if sub_groups[1]:
                            add_groups[2] = sub_groups[1]

                        remove.append(mid_i)

        remove.reverse()
        for index in remove:
            self.new_groups.pop(index)

        # THERE'S A BETTER WAY OF DOING THIS; I JUST DONT KNOW WHAT RIGHT NOW :(
        add_index = bisect_right(self.new_groups, loc)
        for group in add_groups:
            if group:
                self.new_groups.insert(start_i + add_index, group)
                add_index += 1

        # For full string usage.
        for index, char in enumerate(string):
            self.full_str[index] = code + char


def enable_ansi():
    """
    Uses a hack to enable ANSI mode in the Windows console. Does nothing on Linux.
    """
    if system_type() == "Windows":
        # might fuck around
        os.system("")


"""
enable_ansi()
canvas = Canvas(Vector2(40, 26), 1, ())
canvas.render_blank()
import time
import random
ind = 0
for j in range(50):
    canvas.render_all()
    canvas.layers[0].set_char(
        ind % (40 * 26) * 2, "##", "\033[{}m".format(31 + (ind % 12) // 2)
    )
    ind += random.randint(0, 80 * 26)
    canvas.layers[0].set_char(
        ind % (40 * 26) * 2, "##", "\033[{}m".format(31 + (ind % 12) // 2)
    )
    ind += random.randint(0, 80 * 26)


input("")
ind = 0
while True:
    canvas.render_all()
    for yval in range(26):
        if ind % 14 == 13:
            canvas.layers[0].set_string(
                0 + (80 * yval), "---------|" if ind % 2 == 0 else "~~~~~~~~~/", "\033[{}m".format(32)
            )

            canvas.layers[0].set_string(
                20 + (80 * yval), "|---------" if ind % 2 == 0 else "\~~~~~~~~~", "\033[{}m".format(32)
            )

            canvas.layers[0].set_string(
                10 + (80 * yval), "          ", "\033[{}m".format(32)
            )
        else:
            canvas.layers[0].set_string(
                0 + (80 * yval), "---------|" if ind % 2 == 0 else "~~~~~~~~~/", "\033[{}m".format(32)
            )

            canvas.layers[0].set_string(
                20 + (80 * yval), "|---------" if ind % 2 == 0 else "\~~~~~~~~~", "\033[{}m".format(32)
            )

            canvas.layers[0].set_string(
                14 - (1 * (ind % 14)) + (80 * yval), "<{}>".format("--" * (ind % 14)), "\033[{}m".format((34, 32, 33, 31)[int((ind % 14) / 14 * 4)])
            )

    # canvas.layers[0].set_string(
    #     i % (40 * 26), "abcdefghijklmnopqrstuvwxyz", "\033[{}m".format(31 + (i % 12) // 2)
    # )
    ind += 1

# TODO write nicer functions and multilayer support
# multilayer entails searching upwards for groups that intersect; if so, adding them to the layer
# nicer functions means an actual set_char for the canvas that takes in x, y rather than absolute loc
# also add set_string which can take in a longer string, subtracting any intersecting groups
"""