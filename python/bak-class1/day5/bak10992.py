#10992
#별찍기 - 7

n = int(input())
     

for i in range(n):
     if i == n-1:
          print("*"*(2*n-1))
     elif i == 0:
          print("{}{}".format(" "*(n-1), "* "))
     else:
          print("{}{}{}{}".format(" "*(n-i-1), "*"," "*(2*i-1),"* "))
