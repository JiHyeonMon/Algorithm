#11866
#요세푸스 문제 0

N, K = map(int, input().split())
num = [i+1 for i in range(N)]
answer = []
cnt = K
while len(num)>0:
     print('start')
     print(num)
     if cnt>len(num)-1:
          cnt=len(num)-cnt

     else:
          print(num.pop(cnt)+1)
          cnt+=K
     print(num)

print(answer)
