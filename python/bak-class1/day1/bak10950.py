#10950
#두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

num = int(input())

for i in range(0,num):
    a, b = input().split()
    print(int(a)+int(b))
