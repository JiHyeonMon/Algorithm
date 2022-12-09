#9095
#1,2,3 더하기

num = [1, 2, 4]
for i in range(3,12):
     num.append(num[i-1]+num[i-2]+num[i-3])
     
for i in range(int(input())):
     print(num[int(input())-1])
