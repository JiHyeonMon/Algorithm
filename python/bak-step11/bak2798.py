#2798
#카지노에서 제일 인기 있는 게임 블랙잭의 규칙은 상당히 쉽다. 카드의 합이 21을 넘지 않는 한도 내에서, 카드의 합을 최대한 크게 만드는 게임이다. 블랙잭은 카지노마다 다양한 규정이 있다.

n, s = map(int, input().split())
num = list(map(int, input().split()))

sumlist=[]
for i in range(0, n-2):
     for j in range(i+1, n-1):
          for k in range(j+1, n):
               if num[i]+num[j]+num[k]<=s:
                    sumlist.append(num[i]+num[j]+num[k])

sumlist.sort()
print(sumlist[-1])
     
