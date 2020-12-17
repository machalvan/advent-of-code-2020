import copy


def part1(input):
    global min_x, max_x, min_y, max_y, min_z, max_z
    cycles = 6
    x_radius = len(input) // 2
    y_radius = len(input[0]) // 2
    z_radius = 1 // 2

    max_x = x_radius + cycles
    max_y = y_radius + cycles
    max_z = z_radius + cycles

    min_x = -max_x
    min_y = -max_y
    min_z = -max_z

    active = []
    for z, plane in enumerate([input]):
        for y, line in enumerate(plane):
            for x, char in enumerate(line):
                if char == "#":
                    active.append((x - x_radius, y - y_radius, z - z_radius))

    for _ in range(cycles):
        active_copy = copy.deepcopy(active)

        for z in range(min_z, max_z + 1):
            for y in range(min_y, max_y + 1):
                for x in range(min_x, max_x + 1):
                    cube = (x, y, z)
                    active_count = get_active_count(cube, active)

                    if cube in active and not (active_count == 2 or active_count == 3):
                        active_copy.remove(cube)
                    elif cube not in active and active_count == 3:
                        active_copy.append(cube)

        active = copy.deepcopy(active_copy)

    return len(active)


def part2(input):
    global min_x, max_x, min_y, max_y, min_z, max_z, min_w, max_w
    cycles = 6
    x_radius = len(input) // 2
    y_radius = len(input[0]) // 2
    z_radius = w_radius = 1 // 2

    max_x = x_radius + cycles
    max_y = y_radius + cycles
    max_z = z_radius + cycles
    max_w = w_radius + cycles

    min_x = -max_x
    min_y = -max_y
    min_z = -max_z
    min_w = -max_w

    active = []
    for w, grid in enumerate([[input]]):
        for z, plane in enumerate(grid):
            for y, line in enumerate(plane):
                for x, char in enumerate(line):
                    if char == "#":
                        active.append((x - x_radius, y - y_radius, z - z_radius, w - w_radius))

    for _ in range(6):
        active_copy = copy.deepcopy(active)

        for w in range(min_w, max_w + 1):
            for z in range(min_z, max_z + 1):
                for y in range(min_y, max_y + 1):
                    for x in range(min_x, max_x + 1):
                        cube = (x, y, z, w)
                        active_count = get_active_count2(cube, active)

                        if cube in active and not (active_count == 2 or active_count == 3):
                            active_copy.remove(cube)
                        elif cube not in active and active_count == 3:
                            active_copy.append(cube)

        active = copy.deepcopy(active_copy)

    return len(active)


def get_active_count(cube, active):
    x, y, z = cube
    count = 0

    for px in [-1, 0, 1]:
        for py in [-1, 0, 1]:
            for pz in [-1, 0, 1]:
                if px == 0 and py == 0 and pz == 0:
                    continue

                nx = x + px
                ny = y + py
                nz = z + pz

                if min_x <= nx <= max_x and min_y <= ny <= max_y and min_z <= nz <= max_z:
                    if (nx, ny, nz) in active:
                        count += 1
    return count


def get_active_count2(cube, active):
    x, y, z, w = cube
    count = 0

    for px in [-1, 0, 1]:
        for py in [-1, 0, 1]:
            for pz in [-1, 0, 1]:
                for pw in [-1, 0, 1]:
                    if px == 0 and py == 0 and pz == 0 and pw == 0:
                        continue

                    nx = x + px
                    ny = y + py
                    nz = z + pz
                    nw = w + pw

                    if min_x <= nx <= max_x and min_y <= ny <= max_y and min_z <= nz <= max_z and min_w <= nw <= max_w:
                        if (nx, ny, nz, nw) in active:
                            count += 1
    return count


if __name__ == '__main__':
    with open('input.txt') as f:
        file_str = f.read()
        file = file_str.strip().split('\n')

    print(part1(list(file)))
    print(part2(list(file)))
