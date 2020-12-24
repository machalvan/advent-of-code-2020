from copy import deepcopy


def part1(input):
    black_tiles = set()

    dir = ""
    for line in input:
        e = 0
        se = 0

        for ch in line:
            dir += ch

            if dir in ["e", "se", "sw", "w", "nw", "ne"]:
                if dir == "e":
                    e += 1
                elif dir == "se":
                    se += 1
                elif dir == "sw":
                    e -= 1
                    se += 1
                elif dir == "w":
                    e -= 1
                elif dir == "nw":
                    se -= 1
                elif dir == "ne":
                    e += 1
                    se -= 1

                dir = ""

        tile = (e, se)

        if tile in black_tiles:
            black_tiles.remove(tile)
        else:
            black_tiles.add(tile)

    return len(black_tiles)


def part2(input):
    black_tiles = set()

    dir = ""
    for line in input:
        e = 0
        se = 0

        for ch in line:
            dir += ch

            if dir in ["e", "se", "sw", "w", "nw", "ne"]:
                if dir == "e":
                    e += 1
                elif dir == "se":
                    se += 1
                elif dir == "sw":
                    e -= 1
                    se += 1
                elif dir == "w":
                    e -= 1
                elif dir == "nw":
                    se -= 1
                elif dir == "ne":
                    e += 1
                    se -= 1

                dir = ""

        tile = (e, se)

        if tile in black_tiles:
            black_tiles.remove(tile)
        else:
            black_tiles.add(tile)

    limit = 100
    for day in range(100):
        new_black_tiles = deepcopy(black_tiles)

        for e in range(-limit, limit):
            for se in range(-limit, limit):
                tile = (e, se)
                adj = black_adj(tile, black_tiles)

                if tile in black_tiles and (adj == 0 or adj > 2):
                    new_black_tiles.remove(tile)
                elif tile not in black_tiles and adj == 2:
                    new_black_tiles.add(tile)

        black_tiles = new_black_tiles

    return len(black_tiles)


def black_adj(tile, black_tiles):
    adj = 0
    e, se = tile

    if (e + 1, se) in black_tiles:
        adj += 1
    if (e, se + 1) in black_tiles:
        adj += 1
    if (e - 1, se) in black_tiles:
        adj += 1
    if (e, se - 1) in black_tiles:
        adj += 1
    if (e - 1, se + 1) in black_tiles:
        adj += 1
    if (e + 1, se - 1) in black_tiles:
        adj += 1

    return adj


if __name__ == '__main__':
    with open('input.txt') as f:
        file_str = f.read()
        file = file_str.strip().split('\n')

    print(part1(list(file)))
    print(part2(list(file)))
