def solve(ranges):
    total = 0
    
    for rng in ranges.split(","):
        start, end = map(int, rng.strip().split("-"))
        
        start_len = len(str(start))
        end_len = len(str(end))
        
        for digits in range(start_len, end_len + 1):
            if digits % 2 != 0:
                continue
            
            half_len = digits // 2
            for half in range(10**(half_len-1), 10**half_len):
                num = int(str(half) + str(half))
                if start <= num <= end:
                    total += num
    
    return total
with open("input.txt") as f:
    ranges = f.read().strip()
print(solve(ranges))
