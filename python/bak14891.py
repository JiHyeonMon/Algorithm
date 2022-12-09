import collections
import sys

def check_right(which, direction):
     if which == 4 or num[which-1][2] == num[which][6]:
          return 
     
     if num[which-1][2] != num[which][6]:
          check_right(which+1, -direction)
          num[which].rotate(direction)

def check_left(which, direction):
     if which == 1 or num[which+1][6] == num[which][2]:
          return 
     
     if num[which+1][-2] != num[which][2]:
          check_left(which-1, -direction)
          num[which].rotate(direction)

num = []
answer=0
for i in range(4):
     num.append(collections.deque(sys.stdin.readline().strip()))
     print(num[i])

for i in range(int(sys.stdin.readline())):
     n, direction = map(int, sys.stdin.readline().split())
     n-=1
     check_right(n+1, -direction)
     check_left(n-1, -direction)
     num[n].rotate(direction)

for i in range(4):
     print(num[i])
     answer += 2**i * int(num[i][0])
     
print(answer)
