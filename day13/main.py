from math import gcd


def part1(input):
    n = int(input[0])

    times = [int(x) for x in input[1].split(",") if x != 'x']

    res = 0
    g = -1
    for x in times:
        r = n % x
        res = x if r > g else res
        g = max(g, r)

    return res * (res - g)


def part2(input):
    ids = input[1].split(",")
    l = [(k, int(v)) for k, v in enumerate(ids) if v != 'x']

    offset = l[0][0]
    counter = next_id = step = l[0][1]
    while True:
        res = counter - offset

        for index, id in l:
            if (res + index) % id != 0:
                next_id = id
                break
            elif id == next_id:
                step = lcd([id, step])
        else:
            break

        counter += step

    return res


def lcd(l):
    lcm = l[0]
    for x in l[1:]:
        lcm = lcm * x // gcd(lcm, x)
    return lcm


if __name__ == '__main__':
    with open('input.txt') as f:
        file_str = f.read()
        file = file_str.strip().split('\n')

    print(part1(list(file)))
    print(part2(list(file)))
