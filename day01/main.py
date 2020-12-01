def part1(input):
    nums = list(map(int, input))
    for num in nums:
        if 2020 - num in nums:
            return num * (2020 - num)


def part2(input):
    nums = list(map(int, input))
    for num in nums:
        for num2 in nums:
            if 2020 - num - num2 in nums:
                return num * num2 * (2020 - num - num2)


if __name__ == '__main__':
    with open('input.txt') as f:
        file_str = f.read()
        file = file_str.strip().split('\n')

    print(part1(list(file)))
    print(part2(list(file)))
