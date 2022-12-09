#2565
#전깃줄

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr=sorted(arr)

lis = [1]

for i in range(1, N):
     lis.append(1)
     for j in range(i):
          if arr[i][1] > arr[j][1] and lis[j] + 1 > lis[i]:
               lis[i] = lis[j] + 1

print(N - max(lis))

