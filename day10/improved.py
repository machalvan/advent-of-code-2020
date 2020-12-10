def part1(input):
    l = sorted(list(map(int, input)))
    l.insert(0, 0)
    l.append(l[-1] + 3)

    diffs = []
    for i in range(len(l)):
        diffs.append(l[i] - l[i - 1])

    return diffs.count(1) * diffs.count(3)


def part2(input):
    l = sorted(list(map(int, input)))
    l.insert(0, 0)
    l.append(l[-1] + 3)

    visited = {}

    def step(i):
        if i == len(l) - 1:
            return 1
        elif i in visited:
            return visited[i]

        res = 0
        for j in range(i + 1, min(i + 4, len(l))):
            if l[j] - l[i] <= 3:
                res += step(j)

        visited[i] = res
        return res

    return step(0)


if __name__ == '__main__':
    with open('input.txt') as f:
        file_str = f.read()
        file = file_str.strip().split('\n')

    print(part1(list(file)))
    print(part2(list(file)))
