def part1(input):
    n = e = 0
    dir = 1  # North = 0, East = 1, South = 2, West = 3

    for w in input:
        d = w[0]
        u = int(w[1:])

        if d == 'N' or d == 'F' and dir == 0:
            n += u
        elif d == 'E' or d == 'F' and dir == 1:
            e += u
        elif d == 'S' or d == 'F' and dir == 2:
            n -= u
        elif d == 'W' or d == 'F' and dir == 3:
            e -= u
        elif d == 'L':
            dir -= u / 90
        elif d == 'R':
            dir += u / 90

        dir %= 4

    return abs(n) + abs(e)


def part2(input):
    n = e = 0
    wn = 1
    we = 10

    for w in input:
        d = w[0]
        u = int(w[1:])

        if d == 'N':
            wn += u
        elif d == 'E':
            we += u
        elif d == 'S':
            wn -= u
        elif d == 'W':
            we -= u
        elif d == 'L':
            for x in range(u // 90):
                wn, we = we, -wn
        elif d == 'R':
            for x in range(u // 90):
                wn, we = -we, wn
        elif d == 'F':
            n += u * wn
            e += u * we

    return abs(n) + abs(e)


if __name__ == '__main__':
    with open('input.txt') as f:
        file_str = f.read()
        file = file_str.strip().split('\n')

    print(part1(list(file)))
    print(part2(list(file)))
