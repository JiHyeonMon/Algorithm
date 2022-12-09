#11051
#이항 계수 2

import math
N, K = map(int, input().split())
print((math.factorial(N)//(math.factorial(N-K)*math.factorial(K)))%10007)
