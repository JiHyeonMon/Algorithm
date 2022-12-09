#10866
#덱

from collections import deque
import sys
deque = deque()
for i in range(int(sys.stdin.readline())):
     tmp = sys.stdin.readline()
     if tmp[0:6] == 'push_f':
          deque.insert(0, tmp[11:len(tmp)-1])
     if tmp[0:6] == 'push_b':
          deque.append(tmp[10:len(tmp)-1])
     if tmp[0:5] == 'pop_f':
          if not deque:
               print(-1)
          else:
               print(deque.popleft())
     if tmp[0:5] == 'pop_b':
          if not deque:
               print(-1)
          else:
               print(deque.pop())          
     if tmp[0] == 's':
          print(len(deque))
     if tmp[0] == 'e':
          if not deque:
               print(1)
          else:
               print(0)
     if tmp[0] == 'f':
          if not deque:
               print(-1)
          else:
               print(deque[0])
     if tmp[0] == 'b':
          if not deque:
               print(-1)
          else:
               print(deque[-1])
