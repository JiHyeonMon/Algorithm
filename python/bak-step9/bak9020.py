#9020
#골드바흐의 추측

import math
num = int(input())
prime = [2,3]

for i in range(4, 10001):
     t = True
     for j in range(2, int(math.sqrt(i))+1):
          if i%j==0:
               t = False
               break
     if t is True:prime.append(i)

for i in range(0, num):
     n = int(input())
     if n//2 in prime:
          if (n//2)*2 == n:
               print(n//2, n//2)
               continue
     else:
          for i in range(n//2, 2, -1):
               if i in prime:
                    if n-i in prime:
                         print(i, n-i)
                         break
