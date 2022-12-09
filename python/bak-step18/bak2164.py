#2164
#카드2

from collections import deque
num = deque([i+1 for i in range(int(input()))])
while len(num)>1:
     num.popleft()
     num.append(num.popleft())
     
print(num[0])
