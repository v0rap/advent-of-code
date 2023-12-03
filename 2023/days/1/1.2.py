import re

with open("dirty_calibration") as f:
    lines = f.readlines()

LUT = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

total = 0

for line in lines:
    pattern = fr"(?=(\d|{'|'.join(LUT.keys())}))"
    numbers = [LUT.get(x, x) for x in re.findall(pattern, line) if x]
    total += int(numbers[0] + numbers[-1])

print(total)
