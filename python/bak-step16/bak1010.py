#1010
#다리 놓기

import math
for i in range(int(input())):
     a, b = map(int, input().split())
     print(math.factorial(b)//(math.factorial(a)*math.factorial(b-a)))
