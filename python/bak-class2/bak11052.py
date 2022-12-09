#11052
#카드 구매하기


탑다운 방식 
'''     
n = int(input())
price = [0] * (n+1)
card = [0] + list(map(int, input().split()))

def P(n):
     if n == 0:
          return 0
     elif (price[n] > 0):
          return price[n]
     
     for i in range(1, n+1):
               if price[n] < P(n-i) + card[i]:
                    price[n] = P(n-i) + card[i]
     return price[n]
               
print(P(n))
'''


바텀업 방식 
'''
n = int(input())
price = [0] * (n+1)
card = [0] + list(map(int, input().split()))

#1개 살 때, 가격
price[1]=card[1]

for i in range(2, n+1):
     for j in range(1, i+1):
          if price[i]<price[i-j]+card[j]:
               price[i] = price[i-j]+card[j]

print(price[n])
'''
