#2747
#피보나치
import sys

p = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]
for i in range(18, 46):
     p.append(p[i-2]+p[i-1])
     
n = int(sys.stdin.readline())
print(p[n])
