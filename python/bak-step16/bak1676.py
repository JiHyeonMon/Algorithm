#1676
#팩토리얼 0의 개수

import math

N = math.factorial(int(input()))
N = str(N)
answer=0
for i in range(len(N)-1, 0, -1):
     if N[i] == '0':
          answer+=1
     else:
          break

print(answer)
