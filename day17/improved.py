def part1(input):
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
        new_active = set()

        for z in range(min_z, max_z + 1):
            for y in range(min_y, max_y + 1):
                for x in range(min_x, max_x + 1):
                    cube = (x, y, z)
                    active_count = get_active_count(cube, active)

                    if cube in active and (active_count == 2 or active_count == 3):
                        new_active.add(cube)
                    elif cube not in active and active_count == 3:
                        new_active.add(cube)

        active = new_active

    return len(active)


def part2(input):
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
        new_active = set()

        for w in range(min_w, max_w + 1):
            for z in range(min_z, max_z + 1):
                for y in range(min_y, max_y + 1):
                    for x in range(min_x, max_x + 1):
                        cube = (x, y, z, w)
                        active_count = get_active_count2(cube, active)

                        if cube in active and (active_count == 2 or active_count == 3):
                            new_active.add(cube)
                        elif cube not in active and active_count == 3:
                            new_active.add(cube)

        active = new_active

    return len(active)


def get_active_count(cube, active):
    x, y, z = cube
    count = 0

    for px in [-1, 0, 1]:
        for py in [-1, 0, 1]:
            for pz in [-1, 0, 1]:
                if px == 0 and py == 0 and pz == 0:
                    continue

                if (x + px, y + py, z + pz) in active:
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

                    if (x + px, y + py, z + pz, w + pw) in active:
                        count += 1
    return count


if __name__ == '__main__':
    with open('input.txt') as f:
        file_str = f.read()
        file = file_str.strip().split('\n')

    print(part1(list(file)))
    print(part2(list(file)))
