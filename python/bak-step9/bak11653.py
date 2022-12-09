#11653
#소인수분해

n = int(input())
tmp=2

while n>1:
     if n%tmp==0:
          print(tmp)
          n=n//tmp
          tmp=2
     else:
          tmp+=1
