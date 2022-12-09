#2577
#세 개의 자연수 A, B, C가 주어질 때 A×B×C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.

a = int(input())
b = int(input())
c= int(input())
list = [int(0) for i in range(10)]

num = a*b*c

for i in range(1,10):
    if num/10**i<10:
        d = 10**i
        for j in range(0, i+2):
            try:
                list[num//d]+=1
                num = num%d
                d = d//10
            except ZeroDivisionError:
                continue
        break       

for i in range(0,10):
    print(list[i])
