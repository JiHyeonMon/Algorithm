#11444
#피보나치 수6

'''
import sys
p = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]

num = int(sys.stdin.readline())

if num < 18:
     print(p[num])
else:
     for i in range(18, num+1):
          p.append(p[i-1]+p[i-2])
     print(p[num]%1000000007)
'''
