#3036
#링

def gcd(a, b):
     while b!=0:
          n=a%b
          a=b
          b=n
     return a

n = int(input())
num = list(map(int, input().split()))
a = num[0]

for i in range(1, n):
     k = gcd(a, num[i])
     print(str(a//k)+"/"+str(num[i]//k))
