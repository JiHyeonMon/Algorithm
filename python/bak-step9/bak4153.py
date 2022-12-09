#4153
#직각삼각형

while True:
     a = list(map(int, input().split()))
     if 0 in a:
          break

     a.sort()
     if a[2]**2 == a[0]**2 + a[1]**2:
          print("right")
     else:
          print("wrong")
