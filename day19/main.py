import re


def part1(input):
    blocks = [b.split("\n") for b in input]
    d = {}

    for line in blocks[0]:
        k, v = line.split(": ")
        k = int(k)

        if v.startswith('"'):
            d[k] = [v.replace('"', '')]
        else:
            d[k] = [int(x) if x != "|" else "|" for x in v.split()]

    pattern = re.compile(rf"^{solve(0, d)}$")

    return len([line for line in blocks[1] if pattern.match(line)])


def part2(input):
    blocks = [b.split("\n") for b in input]
    d = {}

    for line in blocks[0]:
        k, v = line.split(": ")
        k = int(k)

        if v.startswith('"'):
            d[k] = [v.replace('"', '')]
        else:
            d[k] = [int(x) if x != "|" else "|" for x in v.split()]

    pattern = re.compile(rf"^{solve2(0, d)}$")

    return len([line for line in blocks[1] if pattern.match(line)])


def solve(rule, d):
    reg = ""

    if isinstance(rule, str):
        reg += rule
    else:
        reg += "("
        for rule in d[rule]:
            new_reg = solve(rule, d)
            reg += new_reg
        reg += ")"

    return reg


def solve2(rule, d):
    reg = ""

    if isinstance(rule, str):
        reg += rule
    else:
        rules = d[rule]

        reg += "("
        for r in rules: 
            if rule != 11:
                new_reg = solve2(r, d)
                reg += new_reg
        reg += ")"

        if rule == 8:
            reg += "+"

        if rule == 11:
            A = solve2(rules[0], d)
            B = solve2(rules[1], d)

            c = 10
            reg += "("
            for x in range(1, c):
                reg += f"{A}{{{x}}}{B}{{{x}}}"

                if x < c - 1:
                    reg += "|"
            reg += ")"

    return reg


if __name__ == '__main__':
    with open('input.txt') as f:
        file_str = f.read()
        file = file_str.strip().split('\n\n')

    print(part1(list(file)))
    print(part2(list(file)))
