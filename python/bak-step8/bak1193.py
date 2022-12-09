#1193
#분수 찾기

n  = int(input())
sum = 0
i=1
if n != 1:
     while sum<n:
          sum+=i
          i+=1
     if i%2==0:
          print("{}/{}".format(sum-n+1,i-(sum-n+1)))
     else:
          print("{}/{}".format(i-(sum-n+1),sum-n+1))
else:
     print("1/1")

     


     
