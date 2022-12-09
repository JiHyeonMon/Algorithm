#2750
#N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

size = int(input())
a=[]
for i in range(0, size):
    num = int(input())
    a.append(num)
a.sort()

for i in range(0, size):
    print(a[i])
