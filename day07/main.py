def get_bags_contain(bags, bag):
    if bag not in bags:
        return set()

    res = set(bags[bag])
    for b in bags[bag]:
        res = res.union(get_bags_contain(bags, b))

    return res


def get_contains_count(bags, bag):
    if bag not in bags:
        return 0

    res = 0
    for b in bags[bag]:
        if b[0] != "no":
            res += int(b[0])

            for x in range(int(b[0])):
                res += int(get_contains_count(bags, b[1]))

    return res


def part1(input):
    bags = {}
    for line in input:
        words = line.split()
        value = words[0] + words[1]
        contain = words[4:]

        inside = []
        while len(contain) > 0:
            inside.append([contain[0], contain[1] + contain[2]])
            contain = contain[4:]

        for bag in inside:
            if bag[1] not in bags:
                bags[bag[1]] = [value]
            else:
                bags[bag[1]].append(value)

    return len(get_bags_contain(bags, "shinygold"))


def part2(input):
    bags = {}
    for line in input:
        words = line.split()
        key = words[0] + words[1]
        contain = words[4:]

        values = []
        while len(contain) > 0:
            values.append([contain[0], contain[1] + contain[2]])
            contain = contain[4:]

        bags[key] = values

    return get_contains_count(bags, "shinygold")


if __name__ == '__main__':
    with open('input.txt') as f:
        file_str = f.read()
        file = file_str.strip().split('\n')

    print(part1(list(file)))
    print(part2(list(file)))
