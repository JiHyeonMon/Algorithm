#2108
#통계학

import sys
import math
from collections import Counter

k = int(sys.stdin.readline())
num = [int(sys.stdin.readline()) for i in range(k)]
num_sort = sorted(num)
cnt=Counter(num_sort).most_common()

print(round(sum(num)/len(num)))

print(num_sort[math.floor(len(num)/2)])

if len(cnt)>1:
     if cnt[0][1] == cnt[1][1]:
          print(cnt[1][0])
     else:
          print(cnt[0][0])
else:
     print(cnt[0][0])

print(max(num)-min(num))
