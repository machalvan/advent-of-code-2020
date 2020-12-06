def part1(input):
    ans = 0
    for group in input:
        res = {}
        for line in group.replace("\n", ""):
            res[line] = res.get(line, 0) + 1
        ans += len(res)

    return ans


def part2(input):
    ans = 0
    for group in input:
        line = group.split("\n")

        res = [x for x in line[0]]
        for w in line[1:]:
            if len(line):
                res2 = [x for x in w]
                res = list(set(res) & set(res2))

        ans += len(res)

    return ans


if __name__ == '__main__':
    with open('input.txt') as f:
        file_str = f.read() + "\n"
        file = file_str.strip().split('\n\n')

    print(part1(list(file)))
    print(part2(list(file)))
