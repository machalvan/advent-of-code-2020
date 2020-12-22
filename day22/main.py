from copy import deepcopy


def part1(input):
    stack1, stack2 = [list(map(int, block.split("\n")[1:])) for block in input]

    while True: 
        top1 = stack1.pop(0)
        top2 = stack2.pop(0)

        if top1 > top2:
            stack1.extend([top1, top2])
        else:
            stack2.extend([top2, top1])

        if len(stack1) <= 0 or len(stack2) <= 0:
            winner = stack1 if len(stack2) <= 0 else stack2
            break

    return sum([(i + 1) * card for i, card in enumerate(winner[::-1])])


def part2(input):
    stack1, stack2 = [list(map(int, block.split("\n")[1:])) for block in input]
    history1 = history2 = []

    while True: 
        game(stack1, stack2, history1, history2)

        if len(stack1) <= 0 or len(stack2) <= 0:
            winner = stack1 if len(stack2) <= 0 else stack2
            break

    return sum([(i + 1) * card for i, card in enumerate(winner[::-1])])


def game(stack1, stack2, history1, history2):
    if stack1 in history1 or stack2 in history2:
        return

    history1.append(deepcopy(stack1))
    history2.append(deepcopy(stack2))

    top1 = stack1.pop(0)
    top2 = stack2.pop(0)

    if len(stack1) < top1 or len(stack2) < top2:
        if top1 > top2:
            stack1.extend([top1, top2])
        else:
            stack2.extend([top2, top1])
        return

    sub_stack1 = stack1[:top1]
    sub_stack2 = stack2[:top2]

    h1 = h2 = []
    while True: 
        game(sub_stack1, sub_stack2, h1, h2)

        if len(sub_stack1) <= 0:
            stack2.extend([top2, top1])
            return
        elif len(sub_stack2) <= 0 or sub_stack1 in h1 or sub_stack2 in h2:
            stack1.extend([top1, top2])
            return


if __name__ == '__main__':
    with open('input.txt') as f:
        file_str = f.read()
        file = file_str.strip().split('\n\n')

    print(part1(list(file)))
    print(part2(list(file)))
