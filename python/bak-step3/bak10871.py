#10871
#정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

num, num_max = input().split()
a = list(map(int, input().split()))

total = ""

for i in range(0, int(num)):
    if a[i]<int(num_max):
        total+=str(a[i])+" "

print(total)
        
