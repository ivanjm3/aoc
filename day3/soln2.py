def maxsubseq(line, k):
    stack = []
    for i, ch in enumerate(line):
        remaining = len(line) - i
        while stack and stack[-1] < ch and len(stack) + remaining > k:
            stack.pop()
        if len(stack) < k:
            stack.append(ch)
    return int(''.join(stack[:k]))


def solve(k=12):
    total = 0
    for line in lines:
        line = line.strip()
        if not line:
            continue
        total += maxsubseq(line, k)
    return total

with open('input.txt') as f:
    lines = f.readlines()

print(solve(k=12))

