#2562
#9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.

max = 0
cnt = 0
for i in range(0,9):
    a = int(input())
    if a>max:
        max = a
        cnt = i+1

print(max)
print(cnt)
