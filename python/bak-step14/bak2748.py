#2748
#피보나치 수2

num = [0,1]
for i in range(2, 91):
     num.append(num[i-2]+num[i-1])

print(num[int(input())])

