#1978
#소수 찾기

import math

def Prime(k):
     if k == 1:
          return False
     else:
          for i in range(2, int(math.sqrt(k))+1):
               if k%i==0:
                    return False
     return True

num = int(input())
cnt = 0
p = list(map(int, input().split()))

for i in range(0, num):
     if Prime(p[i]):
          cnt+=1
          
print(cnt)
