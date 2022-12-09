#10818
#N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

num = int(input())
a = list(map(int, input().split()))
min = a[0]
max = a[0]

for i in range(1, num):
    if(a[i]<min):
        min = a[i]
    if(a[i]>max):
        max = a[i]
    
print(min, max)    
