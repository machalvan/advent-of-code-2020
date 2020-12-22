from math import prod


def part1(input):
    blocks = [b.split() for b in input]
    all_blocks = {}

    for block in blocks:
        id = int(block[1][:-1])
        b = block[2:]
        values = [
            list(b[0]),
            [line[-1] for line in b],
            list(b[-1]),
            [line[0] for line in b],
        ]
        all_blocks[id] = [list(row) for row in values]

    connecting_edges = {}
    for k, v in all_blocks.items():
        edges = []
        for k2, v2 in all_blocks.items():
            if k != k2:
                for edge in v:
                    if edge in v2 or edge[::-1] in v2:
                        edges.append(edge)
                        break
        connecting_edges[k] = edges

    return prod([k for k, v in connecting_edges.items() if len(v) == 2])


def part2(input):
    global monster
    monster = [(18, 0), (0, 1), (5, 1), (6, 1), (11, 1), (12, 1), (17, 1), (18, 1), (19, 1), (1, 2), (4, 2), (7, 2), (10, 2), (13, 2), (16, 2)]
    blocks = [b.split() for b in input]

    all_edges = {}
    all_blocks = {}
    for block in blocks:
        id = int(block[1][:-1])
        b = block[2:]
        values = [
            list(b[0]),
            [line[-1] for line in b],
            list(b[-1]),
            [line[0] for line in b],
        ]

        all_edges[id] = values
        all_blocks[id] = [list(row) for row in block[2:]]

    blocks_width = int(len(all_blocks) ** 0.5)

    for id, edges in all_edges.items():
        connecting_edges = []
        for other_id, other_edges in all_edges.items():
            if id == other_id:
                continue

            for i, edge in enumerate(edges):
                if edge in other_edges or edge[::-1] in other_edges:
                    connecting_edges.append(edge)

            if len(connecting_edges) == 2:
                block = all_blocks[id]
                for _ in range(2):
                    for _ in range(4):
                        edges = get_edges(block)
                        right_edge = edges[1]
                        bottom_edge = edges[2]

                        if right_edge in connecting_edges or right_edge[::-1] in connecting_edges:
                            if bottom_edge in connecting_edges or bottom_edge[::-1] in connecting_edges:
                                first_corner = id
                                all_blocks[id] = block
                                all_edges[id] = get_edges(block)

                        block = rotate(block, 1)
                    block = flip(block)

    current_id = first_corner
    left_most_id = current_id
    current_block = all_blocks[current_id]
    arranged_blocks = [current_block]

    while len(arranged_blocks) < len(all_blocks):
        current_edges = get_edges(current_block)
        edge = current_edges[1]  # Right edge
        found = False
        for other_id, other_block in all_blocks.items():
            if other_id == current_id:
                continue

            for _ in range(2):
                for _ in range(4):
                    other_edge = get_edges(other_block)[3]  # Left edge

                    if edge == other_edge:
                        current_id = other_id
                        current_block = other_block

                        all_blocks[other_id] = current_block
                        all_edges[other_id] = get_edges(current_block)
                        arranged_blocks.append(current_block)
                        found = True
                        break

                    other_block = rotate(other_block, 1)

                if found:
                    break

                other_block = flip(other_block)

            if found:
                break

        else:
            current_id = left_most_id

            current_block = all_blocks[current_id]
            current_edges = get_edges(current_block)
            edge = current_edges[2]  # Bottom edge
            found = False

            for other_id, other_block in all_blocks.items():
                if other_id == current_id:
                    continue

                for _ in range(2):
                    for _ in range(4):
                        other_edge = get_edges(other_block)[0]  # Top edge

                        if edge == other_edge:
                            current_id = other_id
                            current_block = other_block

                            all_blocks[other_id] = current_block
                            all_edges[other_id] = get_edges(current_block)
                            arranged_blocks.append(current_block)
                            left_most_id = current_id
                            found = True
                            break

                        other_block = rotate(other_block, 1)

                    if found:
                        break

                    other_block = flip(other_block)

                if found:
                    break

    stripped_blocks = [remove_edges(block) for block in arranged_blocks]
    map = create_map(stripped_blocks, blocks_width)

    for _ in range(2):
        for _ in range(4):
            count = 0
            for y in range(len(map)):
                for x in range(len(map)):
                    if contains_monster(x, y, map):
                        count += 1

            if not count:
                map = rotate(map, 1)

        if not count:
            map = flip(map)

    water_roughness = len([c for r in map for c in r if c == "#"])

    return water_roughness - count * len(monster)


def contains_monster(x, y, map):
    global monster

    try:
        for monster_x, monster_y in monster:
            if map[y + monster_y][x + monster_x] != "#":
                return False
    except IndexError:
        return False

    return True


def create_map(blocks, blocks_width):
    block_size = len(blocks[0])
    block_start = 0
    block_end = blocks_width - 1
    counter = 0

    map = []
    for x in range(blocks_width):
        for r in range(block_size):
            row = []
            for i in range(block_start, block_end + 1):
                for c in range(block_size):
                    row.append(blocks[i][r][c])
                    counter += 1
            map.append(row)
        block_start += blocks_width
        block_end += blocks_width
    return map


def remove_edges(block):
    return [line[1:-1] for line in block[1:-1]]


def get_edges(block):
    return [block[0], [line[-1] for line in block], block[-1], [line[0] for line in block]]


def flip(block):
    # Flip horizontally
    return [row[::-1] for row in block]


def rotate(block, rotation):
    # Rotation (clock-wise)
    # 0 = 0 degrees
    # 1 = 90 degrees
    # 2 = 180 degrees
    # 3 = 270 degrees

    new_block = [[None for _ in range(len(block[0]))] for _ in range(len(block))]
    for x in range(rotation):
        for i, r in enumerate(block):
            for j, c in enumerate(list(r)):
                new_block[j][len(block) - i - 1] = c

    return new_block


# For visualization
def print_block(block):
    for r in block:
        for c in r:
            print(c, end="")
        print()


# For visualization
def print_arranged_blocks(arranged_blocks, block_size=10, blocks_width=12):
    block_start = 0
    block_end = blocks_width - 1
    counter = 0

    for x in range(blocks_width):
        for r in range(block_size):
            for i in range(block_start, block_end + 1):
                for c in range(block_size):
                    print(arranged_blocks[i][r][c], end="")

                    if counter % block_size == block_size - 1:
                        print("  ", end="")
                    counter += 1
            print()
        print()
        block_start += blocks_width
        block_end += blocks_width


if __name__ == '__main__':
    with open('input.txt') as f:
        file_str = f.read()
        file = file_str.strip().split('\n\n')

    print(part1(list(file)))
    print(part2(list(file)))
