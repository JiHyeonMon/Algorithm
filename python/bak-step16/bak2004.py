#2004
#조합 0의 개수

def two(n):
     cnt = 0
     while n!=0:
          n=n//2
          cnt+=n
     return cnt

def five(n):
     cnt = 0
     while n!=0:
          n=n//5
          cnt+=n
     return cnt
     
a, b = map(int, input().split())

if b == 0:
     print(0)
else:
     print(min(two(a)-two(b)-two(a-b), five(a)-five(b)-five(a-b)))
