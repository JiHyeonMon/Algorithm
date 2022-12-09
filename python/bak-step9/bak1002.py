#1002
#터렛

for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5
    
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
        continue
    
    if r1 > d + r2 or r2 > d + r1 or d > r1 + r2:
        print(0)
    elif r1 == d + r2 or r2 == d + r1 or r1 + r2 == d:
        print(1)
    else:
        print(2)
