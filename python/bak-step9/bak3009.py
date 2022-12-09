#3009
#네번째 점 - 세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.

a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))

if a[0]==b[0]:
     x = c[0]
else:
     x = a[0] if a[0]!=c[0] else b[0]

if a[1]==b[1]:
     y = c[1]
else:
     y = a[1] if a[1]!=c[1] else b[1]
print(x, y)
