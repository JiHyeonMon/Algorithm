#18258
#큐 2

from collections import deque
import sys
queue = deque()
for i in range(int(sys.stdin.readline())):
     tmp = sys.stdin.readline()
     if tmp[0:4] == 'push':
          queue.append(int(tmp[5:]))
     if tmp[0:3] == 'pop':
          if not queue:
               print(-1)
          else:
               print(queue.popleft())
     if tmp[0] == 's':
          print(len(queue))
     if tmp[0] == 'e':
          if not queue:
               print(1)
          else:
               print(0)
     if tmp[0] == 'f':
          if not queue:
               print(-1)
          else:
               print(queue[0])
     if tmp[0] == 'b':
          if not queue:
               print(-1)
          else:
               print(queue[-1])
