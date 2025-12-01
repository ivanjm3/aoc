def cntzeros(rots):
    start = 50
    pos = start
    cnt = 0
    zcnt = 0
    
    for line in rots:
        line = line.strip()
        if not line:
            continue
        
        direcn = line[0]
        dist = int(line[1:])
        step = 1 if direcn == 'R' else -1
        
        for _ in range(dist):
            pos = (pos + step) % 100
            if pos == 0:
                zcnt += 1
        
        if pos == 0:
            cnt += 1

    return cnt, zcnt
with open('input.txt', 'r') as file:
    rots = file.readlines()
print(cntzeros(rots))

