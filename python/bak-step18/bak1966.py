#1966
#프린터 큐

from collections import deque
for i  in range(int(input())):
     N, M = map(int, input().split())
     num = deque(list(map(int, input().split())))
     answer = 0
     while True:
          if num[M] != max(num):
               num[num.index(max(num))] = -1
          else:
               if num.count(num[M])>1:
                    
          
          
          
