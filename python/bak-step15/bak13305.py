#13305
#주유소

import sys

N = int(sys.stdin.readline())

oil = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))
answer = price[0]*oil[0]
minP = price[0]

for i in range(1, N-1):
     if minP>price[i]:
          minP = price[i]
     answer += minP * oil[i]
     
print(answer)
