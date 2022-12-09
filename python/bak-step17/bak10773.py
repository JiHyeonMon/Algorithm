#10773
#제로

import sys
num = []
for i in range(int(sys.stdin.readline())):
     tmp = int(sys.stdin.readline())
     if tmp == 0:
          num.pop()
     else:
          num.append(tmp)

print(sum(num))
