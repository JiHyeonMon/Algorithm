#10952
#두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

while(True):
    a, b = input().split()
    if(int(a)==0 and int(b)==0):
        break
    print(int(a)+int(b))
