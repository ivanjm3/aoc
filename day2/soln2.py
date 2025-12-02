def solve(ranges):
    total = 0
    invalid_ids = set()
    
    for rng in ranges.split(","):
        start, end = map(int, rng.strip().split("-"))
        
        start_len = len(str(start))
        end_len = len(str(end))
        
        for digits in range(start_len, end_len + 1):
            for L in range(1, digits // 2 + 1):
                if digits % L != 0:
                    continue
                for block in range(10**(L-1), 10**L):
                    if str(block)[0] == '0':
                        continue
                    num = int(str(block) * (digits // L))
                    if start <= num <= end:
                        invalid_ids.add(num)
    return sum(invalid_ids)
with open("input.txt") as f:
    ranges = f.read().strip()

print(solve(ranges))

