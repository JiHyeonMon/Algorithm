#1931
#회의실 배정

import sys

N = int(sys.stdin.readline())
room = []
for i in range(N):
     room.append(list(map(int, sys.stdin.readline().split())))

room = sorted(room, key = lambda x : (x[1], x[0]))
end = 0
answer = 0
for i, j in room:
     if i >= end:
          answer+=1
          end = j
          
print(answer)
