#1920
#수찾기

'''
import sys
N = int(sys.stdin.readline())
n = list(map(int, sys.stdin.readline().split()))
n.sort()
M = int(sys.stdin.readline())
m = list(map(int, sys.stdin.readline().split()))
m.sort()

for i in m:
     if i in n:
          print(1)
     else:
          print(0)
'''

import sys

def bin(a,x):
    start = 0
    end = len(n)-1

    while start <= end:
        mid = (start + end) // 2
        if x == a[mid]:
            return 1
        elif x > a[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return 0

N = int(input())
n = list(map(int, input().split()))
n = sorted(n)


M = int(input())
m = list(map(int, input().split()))


for i in range(M):
    print(bin(n, m[i]))
