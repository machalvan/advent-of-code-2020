def part1(input):
    return game(input, 2020)


def part2(input):
    return game(input, 30000000)


def game(input, limit):
    ns = list(map(int, input[0].split(",")))
    d = {}

    for i in range(limit):
        s = ns[i] if i < len(ns) else 0 if d[s][1] is None else i - 1 - d[s][1]
        d[s] = (i, None if s not in d else d[s][0])

    return s


if __name__ == '__main__':
    with open('input.txt') as f:
        file_str = f.read()
        file = file_str.strip().split('\n')

    print(part1(list(file)))
    print(part2(list(file)))
