#1929
#소수 구하기 - M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

import math

def Prime(k):
     for i in range(2, int(math.sqrt(k))+1):
          if k%i==0:
               return False
     return True

a, b = map(int, input().split())

for i in range(a, b+1):
     if i == 1:
          pass
     elif i == 2:
          print(i)
     else:
          if Prime(i):
               print(i)
