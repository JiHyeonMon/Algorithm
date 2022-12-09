#2740
#행렬 곱셈

first = []
second = []
answer = []

N, M = map(int, input().split())
for i in range(N):
     first.append(list(map(int, input().split())))
     
M, K = map(int, input().split())
for i in range(M):
     second.append(list(map(int, input().split())))

for i in range(N):
     s = ""
     for j in range(K):
          tmp = 0
          for k in range(M):
               tmp += first[i][k]*second[k][j]
          answer.append(tmp)
          s += str(tmp)+" "
     print(s[0:-1])
