from copy import deepcopy


def get_adj(x, y, grid):
    adj = []

    for px in [-1, 0, 1]:
        for py in [-1, 0, 1]:
            if px == 0 and py == 0:
                continue

            if 0 <= x + px < W and 0 <= y + py < H:
                adj.append(grid[y + py][x + px])
    return adj


def can_see(x, y, px, py, grid):
    if 0 <= x < W and 0 <= y < H:
        c = grid[y][x]
        return c if c in ['L', '#'] else can_see(x + px, y + py, px, py, grid)
    return "."


def get_see(x, y, grid):
    see = []

    for px in [-1, 0, 1]:
        for py in [-1, 0, 1]:
            if px == 0 and py == 0:
                continue

            see.append(can_see(x + px, y + py, px, py, grid))
    return see


def part1(input):
    global W, H
    input = [list(r) for r in input]
    l = deepcopy(input)
    W = len(input[0])
    H = len(input)

    for i in range(100):
        for y in range(H):
            for x in range(W):
                c = l[y][x]
                adj = get_adj(x, y, input)

                if c == 'L' and '#' not in adj:
                    l[y][x] = '#'
                elif c == '#' and adj.count('#') >= 4:
                    l[y][x] = 'L'

        input = deepcopy(l)

    return [c for r in l for c in r].count('#')


def part2(input):
    input = [list(r) for r in input]
    l = deepcopy(input)

    for i in range(100):
        for y in range(H):
            for x in range(W):
                c = l[y][x]
                see = get_see(x, y, input)

                if c == 'L' and '#' not in see:
                    l[y][x] = '#'
                elif c == '#' and see.count('#') >= 5:
                    l[y][x] = 'L'

        input = deepcopy(l)

    return [c for r in l for c in r].count('#')


if __name__ == '__main__':
    with open('input.txt') as f:
        file_str = f.read()
        file = file_str.strip().split('\n')

    print(part1(list(file)))
    print(part2(list(file)))
