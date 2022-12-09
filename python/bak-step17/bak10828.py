#10828
#스택

import sys
stack = []
for i in range(int(sys.stdin.readline())):
     tmp = sys.stdin.readline()
     if tmp[0:4] == 'push':
          stack.append(int(tmp[5:]))
     if tmp[0:3] == 'pop':
          if len(stack)>0:
               print(stack.pop())
          else:
               print(-1)
     if tmp[0] == 's':
          print(len(stack))
     if tmp[0] == 'e':
          if len(stack)>0:
               print(0)
          else:
               print(1)
     if tmp[0] == 't':
          if len(stack)>0:
               print(stack[-1])
          else:
               print(-1)
