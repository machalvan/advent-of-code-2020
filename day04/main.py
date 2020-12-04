import re


def part1(input):
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    valid = 0
    for passport in input:
        res = []
        for field in fields:
            res.append(field in passport)

        if all(res):
            valid += 1

    return valid


def part2(input):
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    valid = 0

    for passport in input:
        present = []
        for field in fields:
            present.append(field in passport)

        if not all(present):
            continue

        res = []
        for w in passport.split():
            f, v = w.split(":")

            if f == fields[0]:
                res.append(1920 <= int(v) <= 2002)

            elif f == fields[1]:
                res.append(2010 <= int(v) <= 2020)

            elif f == fields[2]:
                res.append(2020 <= int(v) <= 2030)

            elif f == fields[3]:
                h = v[:-2]
                unit = v[-2:]
                res.append(h.isnumeric() and
                   (unit == "cm" and 150 <= int(h) <= 193) or
                   (unit == "in" and 59 <= int(h) <= 76)
                )

            elif f == fields[4]:
                res.append(v[0] == "#" and bool(re.compile("[a-f0-9]+").fullmatch(v[1:])))

            elif f == fields[5]:
                res.append(v in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])

            elif f == fields[6]:
                res.append(v.isnumeric() and len(v) == 9)

        if all(res):
            valid += 1

    return valid


if __name__ == '__main__':
    with open('input.txt') as f:
        file_str = f.read()
        file = file_str.strip().split('\n\n')

    print(part1(list(file)))
    print(part2(list(file)))
