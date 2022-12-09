#2581
#소수 - 자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.

import math

def Prime(k):
     for i in range(2, int(math.sqrt(k))+1):
          if k%i==0:
               return False
     return True

a = int(input())
b = int(input())
prime=[]

for i in range(a, b+1):
     if i == 1:
          pass
     elif i == 2:
          prime.append(i)
     else:
          if i%2!=0:
               if Prime(i):
                    prime.append(i)
          
if len(prime)>0:
     print("{}\n{}".format(sum(prime),min(prime)))
else:
     print(-1)
