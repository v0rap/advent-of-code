import re

with open("inputs/1/dirty_calibration") as f:
    lines = f.readlines()

total = 0

for line in lines:
    digits = re.sub(r"\D", "", line)
    total += int(digits[0] + digits[-1])

print(total)
