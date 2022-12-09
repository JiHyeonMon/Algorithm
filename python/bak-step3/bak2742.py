#2742
#자연수 N이 주어졌을 때, N부터 1까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.


num = int(input())
'''
for i in range(1, num+1):
    print(num+1-i)
'''
for i in range(num, 0, -1):
    print(i)

