#9507
#Generations of Tribbles

import sys
for i in range(int(sys.stdin.readline())):
     koong=[1,1,2,4]
     n = int(sys.stdin.readline())
     for j in range(4, n+1):
          koong.append(koong[j-4]+koong[j-3]+koong[j-2]+koong[j-1])
     print(koong[n])
