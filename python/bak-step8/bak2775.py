#2775
#부녀회장이 될테야

l = [[1,2,3,4,5,6,7,8,9,10,11,12,13,14]]
for i in range(1,15):
     ls = []
     for j in range(0,14):
          ls.append(sum(l[i-1][0:j+1]))
     l.append(ls)
     
case = int(input())
for i in range(case):
     k = int(input())
     n = int(input())
     print(l[k][n-1])
