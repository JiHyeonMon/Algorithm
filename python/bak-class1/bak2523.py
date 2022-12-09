#2523
#별찍기 - 13

k = int(input())
for i in range(1, k*2):
     if i<=k:
          print("*"*i)
     else:
          print("*"*(k*2-i))
