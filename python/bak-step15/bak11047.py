#11047
#동전 0

N, price = map(int, input().split())
cnt = 0
money = []
for i in range(N):
     money.append(int(input()))

for i in range(N-1, -1, -1):
     if price == 0:
          break
     if money[i]>price:
          continue
     cnt+=price//money[i]
     price%=money[i]

print(cnt)
