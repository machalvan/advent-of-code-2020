import copy


def get_adj(x, y, w, h, input):
    n = []

    if x > 0:
        n.append((x - 1, y))
        if y > 0:
            n.append((x - 1, y - 1))
        if y < h - 1:
            n.append((x - 1, y + 1))

    if x < w - 1:
        n.append((x + 1, y))
        if y > 0:
            n.append((x + 1, y - 1))
        if y < h - 1:
            n.append((x + 1, y + 1))

    if y > 0:
        n.append((x, y - 1))

    if y < h - 1:
        n.append((x, y + 1))

    return [input[c[1]][c[0]] for c in n]


def see(x, y, input):
    c = input[y][x]
    if c in ['L', '#']:
        return c
    return "."


def get_see(x, y, w, h, input):
    n = []
    m = "."

    px = x - 1
    py = y
    while px >= 0 and m == ".":
        m = see(px, py, input)
        px -= 1
    n.append(m)
    m = "."

    px = x + 1
    py = y
    while px < w and m == ".":
        m = see(px, py, input)
        px += 1
    n.append(m)
    m = "."

    px = x
    py = y - 1
    while py >= 0 and m == ".":
        m = see(px, py, input)
        py -= 1
    n.append(m)
    m = "."

    px = x
    py = y + 1
    while py < h and m == ".":
        m = see(px, py, input)
        py += 1
    n.append(m)
    m = "."

    px = x - 1
    py = y - 1
    while px >= 0 and py >= 0 and m == ".":
        m = see(px, py, input)
        px -= 1
        py -= 1
    n.append(m)
    m = "."

    px = x + 1
    py = y - 1
    while px < w and py >= 0 and m == ".":
        m = see(px, py, input)
        px += 1
        py -= 1
    n.append(m)
    m = "."

    px = x - 1
    py = y + 1
    while px >= 0 and py < h and m == ".":
        m = see(px, py, input)
        px -= 1
        py += 1
    n.append(m)
    m = "."

    px = x + 1
    py = y + 1
    while px < w and py < h and m == ".":
        m = see(px, py, input)
        px += 1
        py += 1
    n.append(m)

    return n


def part1(input):
    input = [[char for char in row] for row in input]
    w = len(input[0])
    h = len(input)
    l = copy.deepcopy(input)

    for i in range(100):
        y = 0
        while y < h:
            x = 0
            while x < w:
                c = input[y][x]

                if c == 'L' and '#' not in get_adj(x, y, w, h, input):
                    l[y][x] = '#'
                elif c == '#' and len([x for x in get_adj(x, y, w, h, input) if x == '#']) >= 4:
                    l[y][x] = 'L'

                x += 1
            y += 1
        input = copy.deepcopy(l)

    res = 0
    for r in l:
        for c in r:
            if c == '#':
                res += 1

    return res


def part2(input):
    input = [[char for char in row] for row in input]
    w = len(input[0])
    h = len(input)
    l = copy.deepcopy(input)

    for i in range(100):
        y = 0
        while y < h:
            x = 0
            while x < w:
                c = input[y][x]

                if c == 'L' and '#' not in get_see(x, y, w, h, input):
                    l[y][x] = '#'
                elif c == '#' and len([x for x in get_see(x, y, w, h, input) if x == '#']) >= 5:
                    l[y][x] = 'L'

                x += 1
            y += 1
        input = copy.deepcopy(l)

    res = 0
    for r in l:
        for c in r:
            if c == '#':
                res += 1

    return res


if __name__ == '__main__':
    with open('input.txt') as f:
        file_str = f.read()
        file = file_str.strip().split('\n')

    print(part1(list(file)))
    print(part2(list(file)))
