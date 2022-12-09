#1977
#완전 제곱수
import math

n = math.ceil(math.sqrt(int(input())))
m = math.floor(math.sqrt(int(input())))
sum=0
for i in range(n, m+1):
     sum+=i*i

if sum == 0:
     print(-1)
else:
     print(sum)
     print(n*n)
