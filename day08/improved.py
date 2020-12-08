def part1(input):
    p = 0
    g = 0
    visited = []

    while p < len(input):
        if p in visited:
            break

        visited.append(p)
        line = input[p]
        op, v = line.split()
        v = int(v)

        if op == 'acc':
            g += v
        elif op == 'jmp':
            p += v
            continue
        elif op == 'nop':
            pass

        p += 1
    return g


def part2(input):
    p = 0
    g = 0
    visited = []
    c = None

    while p < len(input):
        if p in visited and c:
            p, op, v, g = c
            c = None

            if op == 'jmp':
                p += v
                continue
            elif op == 'nop':
                pass

            p += 1
            continue

        visited.append(p)
        line = input[p]
        op, v = line.split()
        v = int(v)

        if op == 'acc':
            g += v
        elif op == 'jmp':
            if not c:
                c = (p, op, v, g)
                p += 1
                continue

            p += v
            continue

        elif op == 'nop':
            if not c:
                c = (p, op, v, g)
                p += v
                continue

        p += 1
    return g


if __name__ == '__main__':
    with open('input.txt') as f:
        file_str = f.read()
        file = file_str.strip().split('\n')

    print(part1(list(file)))
    print(part2(list(file)))
