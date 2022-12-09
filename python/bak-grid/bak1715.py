#1715
#카드 정렬하기

import sys
import heapq

card = []
answer = 0
for i in range(int(sys.stdin.readline())):
     heapq.heappush(card, int(sys.stdin.readline()))

card.sort()
while len(card)>1:
     tmp1 = heapq.heappop(card)
     tmp2 = heapq.heappop(card)
     answer+=tmp1+tmp2
     heapq.heappush(card, tmp1+tmp2)

print(answer)
