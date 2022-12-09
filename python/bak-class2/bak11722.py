#11722
#가장 긴 감소하는 부분 수열

n = int(input())
num = list(map(int, input().split()))

dp = [1 for i in range(n)]
'''
for i in range(n):
    for j in range(i):
        if num[i] < num[j]:
            dp[i] = max(dp[i], dp[j] + 1)
            
print(max(dp))
print(dp)

'''
for i in range(1, n):
    s = []
    for j in range(i):
        if num[j] > num[i]:
            s.append(dp[j])
    if not s:
        continue
    else:
        dp[i] += max(s)
        
print(max(dp))
print(dp)
