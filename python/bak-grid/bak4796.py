#4796
#캠핑
i= 1
while True:
     x, y, z = map(int, input().split())
     answer = 0
     
     if x==0:
          break
     
     answer = z//y * x + min(z%y, x)
     
     print("Case "+str(i)+": "+str(answer))
     i+=1
