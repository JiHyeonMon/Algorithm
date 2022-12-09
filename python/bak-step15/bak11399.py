#11399
#ATM

N = int(input())
time = sorted(list(map(int, input().split())))
total = 0
for i in range(N-1, -1, -1):
     total+=time[i]*(N-i)
print(total)
