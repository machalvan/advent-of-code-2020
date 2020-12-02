def part1(input):
    valid = 0
    for line in input:
        parts = line.split(" ")
        min = int(parts[0].split("-")[0])
        max = int(parts[0].split("-")[1])
        char = parts[1][0]
        pwd = parts[2]

        if min <= pwd.count(char) <= max:
            valid += 1
    return valid


def part2(input):
    valid = 0
    for line in input:
        parts = line.split(" ")
        min = int(parts[0].split("-")[0])
        max = int(parts[0].split("-")[1])
        char = parts[1][0]
        pwd = parts[2]

        min_match = pwd[min - 1] == char
        max_match = pwd[max - 1] == char
        if (min_match and not max_match) or (not min_match and max_match):
            valid += 1
    return valid


if __name__ == '__main__':
    with open('input.txt') as f:
        file_str = f.read()
        file = file_str.strip().split('\n')

    print(part1(list(file)))
    print(part2(list(file)))
