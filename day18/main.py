def part1(input):
    return sum([solve(line.replace(" ", "")) for line in input]) 


def part2(input):
    return sum([solve2(line.replace(" ", "")) for line in input])


def solve(exp):
    c = 0
    res = None
    sign = None

    while c < len(exp):
        ch = exp[c]

        if ch.isnumeric():
            ch = int(ch)
            if res:
                if sign == "+":
                    res += ch
                elif sign == "*":
                    res *= ch
            else:
                res = ch
        elif ch == "+":
            sign = "+"
        elif ch == "*":
            sign = "*"
        elif ch == "(":
            inner_exp = ""
            stack = 1
            c += 1
            ch = exp[c]

            while c < len(exp):
                if ch == ")":
                    stack -= 1
                elif ch == "(":
                    stack += 1

                if stack <= 0:
                    break
                
                inner_exp += ch
                c += 1
                ch = exp[c]

            ch = solve(inner_exp)

            if res:
                if sign == "+":
                    res += ch
                elif sign == "*":
                    res *= ch
            else:
                res = ch
        c += 1
        
    return res


def solve2(exp):
    c = 0
    mem = None
    sign = None

    while c < len(exp):
        ch = exp[c]

        if ch.isnumeric():
            ch = int(ch)
            if mem:
                if sign == "+":
                    mem += ch
                elif sign == "*":
                    if c < len(exp):
                        inner_exp = exp[c:]
                        ch = solve2(inner_exp)

                    return mem * ch
            else:
                mem = ch
        elif ch == "+":
            sign = "+"
        elif ch == "*":
            sign = "*"
        elif ch == "(":
            inner_exp = ""
            stack = 1
            c2 = c
            c += 1
            ch = exp[c]

            while c < len(exp):
                if ch == ")":
                    stack -= 1
                elif ch == "(":
                    stack += 1

                if stack <= 0:
                    break

                inner_exp += ch
                c += 1
                ch = exp[c]

            ch = solve2(inner_exp)

            if mem:
                if sign == "+":
                    mem += ch
                elif sign == "*":
                    if c2 < len(exp):
                        inner_exp = exp[c2:]
                        ch = solve2(inner_exp)

                    return mem * ch
            else:
                mem = ch
        c += 1

    return mem


if __name__ == '__main__':
    with open('input.txt') as f:
        file_str = f.read()
        file = file_str.strip().split('\n')

    print(part1(list(file)))
    print(part2(list(file)))
