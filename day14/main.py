def part1(input):
    mem = {}
    mask = None

    for line in input:
        words = line.split(" = ")

        if words[0] == "mask":
            mask = words[1]
            continue

        adr = words[0][4:-1]
        mem[adr] = masked(mask, to_bin(words[1]))

    return sum([to_dec(mem[adr]) for adr in mem])


def part2(input):
    mem = {}
    mask = None

    for line in input:
        words = line.split(" = ")

        if words[0] == "mask":
            mask = words[1]
            continue

        adr = words[0][4:-1]
        bin = masked2(mask, to_bin(adr))

        for a in get_addresses(bin):
            mem[to_dec(a)] = int(words[1])

    return sum([mem[adr] for adr in mem])


def to_bin(dec):
    return '{:036b}'.format(int(dec))


def to_dec(bin):
    return int(bin, 2)


def masked(m, v):
    masked = ''
    for i, c in enumerate(list(m)):
        masked += v[i] if c == 'X' else c
    return masked


def masked2(m, v):
    masked = ''
    for i, c in enumerate(list(m)):
        masked += v[i] if m[i] == '0' else '1' if m[i] == '1' else 'X'
    return masked


def get_addresses(bin):
    addresses = ['']
    for i, c in enumerate(list(bin)):
        if c == 'X':
            addresses = [l + x for l in addresses for x in ('0', '1')]
        else:
            addresses = [l + c for l in addresses]
    return addresses


if __name__ == '__main__':
    with open('input.txt') as f:
        file_str = f.read()
        file = file_str.strip().split('\n')

    print(part1(list(file)))
    print(part2(list(file)))
