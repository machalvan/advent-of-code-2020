import math


def part1(input):
    x = trees = 0

    for line in input[1:]:
        x += 3
        char = line[x % len(input[0])]
        if char == "#":
            trees += 1

    return trees


def part2(input):
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    slopes_trees = []

    for slope in slopes:
        x = y = trees = 0

        while y < len(input) - 1:
            x += slope[0]
            y += slope[1]
            line = input[y]
            char = line[x % len(input[0])]

            if char == "#":
                trees += 1

        slopes_trees.append(trees)

    return math.prod(slopes_trees)


if __name__ == '__main__':
    with open('input.txt') as f:
        file_str = f.read()
        file = file_str.strip().split('\n')

    print(part1(list(file)))
    print(part2(list(file)))
