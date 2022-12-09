#10951
#두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break

'''
테스트 케이스 개수가 정해지지 않았기 때문에
try: 변수 A,B에 int형이 들어간다면, A+B의 값을 출력한다.
except: try에 대한 에러가 발생한 경우(ex. a 1, 3, 2 ㄱ 입력)
break: while문을 멈춘다.
'''
