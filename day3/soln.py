def maxbank(line):
    digits = [int(c) for c in line.strip()]
    best = -1

    for i in range(len(digits)):
        for j in range(i+1, len(digits)):
            value = 10 * digits[i] + digits[j]
            if value > best:
                best = value
    return best
def solve(lines):
    total = 0
    for line in lines:
        line = line.strip()
        if not line:
            continue
        total += maxbank(line)
    return total
with open("input.txt") as f:
    lines = f.readlines()
print(solve(lines))

