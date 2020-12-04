import re


def part1(input):
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    valid = 0
    for passport in input:
        if all([field in passport for field in fields]):
            valid += 1

    return valid


def part2(input):
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    num_valid = 0

    for passport in input:
        if not all([field in passport for field in fields]):
            continue

        valid = True
        for w in passport.split():
            f, v = w.split(":")

            if f == fields[0] and 1920 <= int(v) <= 2002:
                continue

            elif f == fields[1] and 2010 <= int(v) <= 2020:
                continue

            elif f == fields[2] and 2020 <= int(v) <= 2030:
                continue

            elif f == fields[3]:
                h = v[:-2]
                unit = v[-2:]
                if (h.isnumeric() and
                   (unit == "cm" and 150 <= int(h) <= 193) or
                   (unit == "in" and 59 <= int(h) <= 76)
                ):
                    continue

            elif f == fields[4] and v[0] == "#" and bool(re.compile("[a-f0-9]+").fullmatch(v[1:])):
                continue

            elif f == fields[5] and v in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                continue

            elif f == fields[6] and v.isnumeric() and len(v) == 9:
                continue

            elif f == "cid":
                continue

            valid = False

        if valid:
            num_valid += 1

    return num_valid


if __name__ == '__main__':
    with open('input.txt') as f:
        file_str = f.read()
        file = file_str.strip().split('\n\n')

    print(part1(list(file)))
    print(part2(list(file)))
