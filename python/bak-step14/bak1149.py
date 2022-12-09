#1463
#1로 만들기 
'''
1=1
2=1
3=1
4=2 *2 *2 / *3 +1
5=3 *2 *2 +1 / *3 *2 +1
6=2 *3 *3
7=3 *3 *2 +1
8= *3 *2 +1 +1
'''

'''
n = int(input())
cnt= 0
tmp = 1

while tmp>=n:
     tmp*=3
     cnt+=1

if tmp==n:
     cnt-=1
else:
'''
     
'''
while n!=1:
     if n%3==0:
          n=n//3
     elif n%2==0:
          n=n//2
     else:
          n-=1

     if n==1:
          if cnt==0:
               cnt=1
          break
     
     cnt+=1

print(cnt)

'''

n=int(input())
 
dp=[ 0 for _ in range(n+2) ]
dp[2]=1
 
for i in range(2, len(dp)):
 
    dp[i]=dp[i-1]+1
 
    if i%3==0:
        if dp[i]> dp[int(i/3)]+1:
            dp[i]=dp[int(i/3)]+1
    if i%2==0:
        if dp[i]> dp[int(i/2)]+1:
            dp[i] =dp[int(i/2)]+1
 
print(dp[n])
 
