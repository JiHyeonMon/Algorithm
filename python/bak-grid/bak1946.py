#1946
#신입사원
import sys
for i in range(int(sys.stdin.readline())):
     score=[]
     answer=1
     for j in range(int(sys.stdin.readline())):
          score.append(list(map(int, sys.stdin.readline().split())))
     score.sort()
     mini = score[0][1]
     for j in range(1, len(score)):
          if score[j][1]<mini:
               answer+=1
               mini = score[j][1]
          
     print(answer)
