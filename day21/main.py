def part1(input):
    alls_in_ings = {}
    all_ings = []

    for line in input:
        line = line.replace("(", "").replace(")", "").replace(",", "")
        ings, alls = line.split(" contains ")
        ings = ings.split()
        alls = alls.split()
        all_ings.extend(ings)

        for all in alls:
            if all in alls_in_ings:
                alls_in_ings[all] = list(set(alls_in_ings[all]) & set(ings))
            else:
                alls_in_ings[all] = ings

    contains = [v for k, v in alls_in_ings.items()]
    contains = [item for sublist in contains for item in sublist]

    not_contains = set(all_ings).difference(contains)

    return len([ing for ing in all_ings if ing in not_contains])


def part2(input):
    alls_in_ings = {}
    all_ings = []

    for line in input:
        line = line.replace("(", "").replace(")", "").replace(",", "")
        ings, alls = line.split(" contains ")
        ings = ings.split()
        alls = alls.split()
        all_ings.extend(ings)

        for all in alls:
            if all in alls_in_ings:
                alls_in_ings[all] = list(set(alls_in_ings[all]) & set(ings))
            else:
                alls_in_ings[all] = ings

    sorted_alls = {all: ings for all, ings in sorted(alls_in_ings.items(), key=lambda item: len(item[1]))}

    ing_to_all = {}
    for all, ings in sorted_alls.items():
        for ing in ings:
            if ing not in ing_to_all:
                ing_to_all[ing] = all

    sorted_ing_to_all = {ing: all for ing, all in sorted(ing_to_all.items(), key=lambda item: item[1])}

    return ",".join([ing for ing, all in sorted_ing_to_all.items()])


if __name__ == '__main__':
    with open('input.txt') as f:
        file_str = f.read()
        file = file_str.strip().split('\n')

    print(part1(list(file)))
    print(part2(list(file)))
