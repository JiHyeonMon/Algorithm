#11050
#이항 계수

import math
N, K = map(int, input().split())
print(math.factorial(N)//(math.factorial(N-K)*math.factorial(K)))
