#2292
#벌집

'''
n = int(input())
i=0
for j in range(1,n):
     if 6*i+2<=n and n<=6*(i+j)+1:
          print(j+1)
          break
     i += j
'''

n = int(input())
i=1
sum = 1
if n!=1:
     while sum<n:
          sum += 6*i
          i+=1

print(i)
