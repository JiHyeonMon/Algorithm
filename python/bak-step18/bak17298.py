#17298
#오큰수

import sys
N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
stack = []
ans = [-1 for _ in range(N)]

for i in range(len(num)):
    while len(stack)!=0 and num[stack[-1]] < num[i]:
        ans[stack.pop()] = num[i]
    stack.append(i)
print(*ans)
