#10870
#피보나치 수 5 - n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.

p = [0,1]
for i in range(2, 21):
     p.append(p[i-2]+p[i-1])

print(p[int(input())])
