def part1(input):
    l = [x for x in map(int, input)]

    for i, item in enumerate(l):
        if i - 25 < 0:
            continue

        sums = []
        for x in range(i - 25, i):
            for y in range(x + 1, i):
                sums.append(l[x] + l[y])

        if item not in sums:
            return item


def part2(input):
    l = [x for x in map(int, input)]
    target = 27911108

    for i in range(0, len(l)):
        sums = []

        for x in range(i, len(l)):
            sums.append(l[x])

            if sum(sums) == target:
                return min(sums) + max(sums)
            elif sum(sums) > target:
                break


if __name__ == '__main__':
    with open('input.txt') as f:
        file_str = f.read()
        file = file_str.strip().split('\n')

    print(part1(list(file)))
    print(part2(list(file)))
