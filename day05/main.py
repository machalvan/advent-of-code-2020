import math


def part1(input):
    max_id = 0

    for line in input:
        f = 0
        b = 127
        l = 0
        r = 7

        for c in line:
            if c == "F":
                b = (f + b) // 2
            elif c == "B":
                f = math.ceil((f + b) / 2)

            else:
                if c == "L":
                    r = (l + r) // 2
                elif c == "R":
                    l = math.ceil((l + r) / 2)

        id = f * 8 + l
        max_id = max(max_id, id)

    return max_id


def part2(input):
    max_id = 0
    ids = []

    for line in input:
        f = 0
        b = 127
        l = 0
        r = 7

        for c in line:
            if c == "F":
                b = (f + b) // 2
            elif c == "B":
                f = math.ceil((f + b) / 2)

            else:
                if c == "L":
                    r = (l + r) // 2
                elif c == "R":
                    l = math.ceil((l + r) / 2)

        id = f * 8 + l
        ids.append(id)
        max_id = max(max_id, id)

    for x in range(0, max_id):
        if x not in ids and x - 1 in ids and x + 1 in ids:
            return x


if __name__ == '__main__':
    with open('input.txt') as f:
        file_str = f.read()
        file = file_str.strip().split('\n')

    print(part1(list(file)))
    print(part2(list(file)))
