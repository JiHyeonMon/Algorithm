#2753
#연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력하는 프로그램을 작성하시오.

a = int(input())

if(a%4==0):
    if(a%100!=0 or a%400==0):
        print("1")
    else:
        print("0")
else:
    print("0")
