target = None


def part1(input):
    global target
    l = [x for x in map(int, input)]

    for i, item in enumerate(l):
        if i - 25 < 0:
            continue

        sums = []
        for x in range(i - 25, i):
            for y in range(x + 1, i):
                sums.append(l[x] + l[y])

        if item not in sums:
            target = item
            return item


def part2(input):
    assert target is not None, "Part 1 is missing answer"

    l = [x for x in map(int, input)]

    for x in range(len(l)):
        for y in range(x + 1, len(l)):
            items = l[x:y]

            if sum(items) == target:
                return min(items) + max(items)
            elif sum(items) > target:
                break


if __name__ == '__main__':
    with open('input.txt') as f:
        file_str = f.read()
        file = file_str.strip().split('\n')

    print(part1(list(file)))
    print(part2(list(file)))
