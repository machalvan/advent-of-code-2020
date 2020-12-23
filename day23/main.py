def part1(input):
    l = []
    for line in input:
        for ch in line:
            l.append(int(ch))

    for x in range(100):
        i = x % len(l)
        cur = l[i]
        rem = (l * 2)[i + 1:i + 4]

        for r in rem:
            l.remove(r)

        dest = cur - 1
        if dest < min(l):
            dest = max(l)

        while dest in rem:
            dest -= 1
            if dest < min(l):
                dest = max(l)

        dest_index = l.index(dest)
        l = l[:dest_index + 1] + rem + l[dest_index + 1:]

        shift = l.index(cur) - i
        l = l[shift:] + l[:shift]

    index = l.index(1)
    return "".join([str(x) for x in l[index + 1:] + l[:index]])


def part2(input):
    l = []
    d = {}

    for line in input:
        for ch in line:
            l.append(int(ch))

    l += list(range(max(l) + 1, 1_000_000 + 1))

    for i, x in enumerate(l):
        d[x] = l[(i + 1) % len(l)]

    cur = l[0]
    min_l = min(l)
    max_l = max(l)
    for p in range(10_000_000):
        rem1 = d[cur]
        rem2 = d[rem1]
        rem3 = d[rem2]

        dest = cur - 1
        if dest < min_l:
            dest = max_l

        while dest in [rem1, rem2, rem3]:
            dest -= 1
            if dest < min_l:
                dest = max_l

        d[cur] = d[rem3]
        d[rem3] = d[dest]
        d[dest] = rem1

        cur = d[cur]

    return d[1] * d[d[1]]


if __name__ == '__main__':
    with open('input.txt') as f:
        file_str = f.read()
        file = file_str.strip().split('\n')

    print(part1(list(file)))
    print(part2(list(file)))
