#9012
#괄호
import sys
for i in range(int(sys.stdin.readline())):
     TF = True
     num = 0
     tmp = sys.stdin.readline()
     for j in range(len(tmp)):
          if num<0:
               TF=False
               break
          if tmp[j] == '(':
               num+=1
          else:
               num-=1
     if num == -1:
          if TF:
               print("YES")
          else:
               print("NO")
     else:
          print("NO")
