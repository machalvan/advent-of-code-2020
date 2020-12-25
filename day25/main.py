def part1(input):
    card_pub, door_pub = list(map(int, input))
    val = 1
    sn = 7
    den = 20201227

    card_ls = 0
    while val != card_pub:
        val *= sn
        val %= den
        card_ls += 1

    val = 1
    sn = door_pub
    for _ in range(card_ls):
        val *= sn
        val %= den

    return val


def part2(input):
    return


if __name__ == '__main__':
    with open('input.txt') as f:
        file_str = f.read()
        file = file_str.strip().split('\n')

    print(part1(list(file)))
    print(part2(list(file)))
