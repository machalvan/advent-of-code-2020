def part1(input):
    N = E = 0
    di = 1  # North = 0, East = 1, South = 2, West = 3

    for w in input:
        d = w[0]
        u = int(w[1:])

        if d == 'N':
            N += u
        elif d == 'E':
            E += u
        elif d == 'S':
            N -= u
        elif d == 'W':
            E -= u
        elif d == 'L':
            if u == 90:
                di -= 1
            elif u == 180:
                di -= 2
            elif u == 270:
                di -= 3

        elif d == 'R':
            if u == 90:
                di += 1
            elif u == 180:
                di += 2
            elif u == 270:
                di += 3

        elif d == 'F':
            if di == 0:
                N += u
            elif di == 1:
                E += u
            elif di == 2:
                N -= u
            elif di == 3:
                E -= u

        di %= 4

    return abs(N) + abs(E)


def part2(input):
    N = E = 0
    wN = 1
    wE = 10

    for w in input:
        d = w[0]
        u = int(w[1:])

        if d == 'N':
            wN += u
        elif d == 'E':
            wE += u
        elif d == 'S':
            wN -= u
        elif d == 'W':
            wE -= u
        elif d == 'L':
            if u == 90:
                wN, wE = wE, -wN
            elif u == 180:
                wN, wE = -wN, -wE
            elif u == 270:
                wN, wE = -wE, wN

        elif d == 'R':
            if u == 90:
                wN, wE = -wE, wN
            elif u == 180:
                wN, wE = -wN, -wE
            elif u == 270:
                wN, wE = wE, -wN

        elif d == 'F':
            N += u * wN
            E += u * wE

    return abs(N) + abs(E)


if __name__ == '__main__':
    with open('input.txt') as f:
        file_str = f.read()
        file = file_str.strip().split('\n')

    print(part1(list(file)))
    print(part2(list(file)))
