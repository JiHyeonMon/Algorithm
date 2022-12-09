#4948
#베르트랑 공존
import math

def isPrime(num):
    if num == 1: return False

    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0: return False

    return True


li = list(range(2,246912))
prime_li = []
for i in li:
    if isPrime(i):
        prime_li.append(i)

while(1):
    answer = 0
    n = int(input())
    if n == 0: break

    for i in prime_li:
        if n < i <= n*2:
            answer += 1

    print(answer)
