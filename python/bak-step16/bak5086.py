#5086
#배수와 약수

while True:
     a, b = map(int, input().split())
     if a==0:
          break
     elif a%b == 0:
          print("multiple")
     elif b%a == 0:
          print("factor")
     else:
          print("neither")
