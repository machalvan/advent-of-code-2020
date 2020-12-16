from math import prod


def part1(input):
    blocks = [b.split('\n') for b in input]
    allowed = []

    for line in blocks[0]:
        field, ranges = line.strip().split(":")
        ranges = ranges.split(" or ")

        for r in ranges:
            lo, hi = list(map(int, r.split("-")))
            allowed += list(range(lo, hi + 1))

    res = 0
    for line in blocks[2][1:]:
        line = list(map(int, line.split(",")))
        res += sum([val for val in line if val not in allowed])

    return res


def part2(input):
    blocks = [b.split('\n') for b in input]
    allowed = []

    d = {}
    for line in blocks[0]:
        field, ranges = line.strip().split(":")
        ranges = ranges.split(" or ")

        range_list = []
        for r in ranges:
            lo, hi = list(map(int, r.split("-")))
            range_list += list(range(lo, hi + 1))

        d[field] = range_list
        allowed += range_list

    your_ticket = list(map(int, blocks[1][1].split(",")))

    pos_values = {}
    for line in blocks[2][1:]:
        ticket = line.split(",")
        ticket = list(map(int, ticket))

        if all(val in allowed for val in ticket):
            for i, val in enumerate(ticket):
                if i in pos_values:
                    pos_values[i].append(val)
                else:
                    pos_values[i] = [val]

    potentials = {}
    for pos, values in pos_values.items():
        pot = []
        for field in d:
            if all(val in d[field] for val in values):
                pot.append(field)

        potentials[pos] = pot

    potentials = {pos: fields for pos, fields in sorted(potentials.items(), key=lambda item: len(item[1]))}

    positions = {}
    for pos, fields in potentials.items():
        for field in fields:
            if field not in positions:
                positions[field] = pos
        
    return prod([your_ticket[v] for k, v in positions.items() if k.startswith('departure')])


if __name__ == '__main__':
    with open('input.txt') as f:
        file_str = f.read()
        file = file_str.strip().split('\n\n')

    print(part1(list(file)))
    print(part2(list(file)))
