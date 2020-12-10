def part1(input):
    l = list(map(int, input))
    l = sorted(set(l))
    l.append(l[-1] + 3)

    prev = 0
    diffs = []
    while len(l) > 0:
        diffs.append(l[0] - prev)
        prev = l[0]
        l.remove(l[0])

    return diffs.count(1) * diffs.count(3)


def part2(input):
    l = list(map(int, input))
    l = sorted(set(l))
    l.insert(0, 0)
    l.append(l[-1] + 3)

    p = 1
    c = 0
    res = 1
    while p < len(l) - 1:
        removable = l[p + 1] - l[p - 1] <= 3
        if removable:
            c += 1
        if not removable or p == len(l) - 2:
            if c == 1:
                res *= 2 ** 1
            elif c == 2:
                res *= 2 ** 2
            elif c >= 3:
                res *= 2 ** 3 - 1
            c = 0
        p += 1

    return res


if __name__ == '__main__':
    with open('input.txt') as f:
        file_str = f.read()
        file = file_str.strip().split('\n')

    print(part1(list(file)))
    print(part2(list(file)))
