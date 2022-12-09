#11718
#입력 받은 대로 출력하는 프로그램을 작성하시오.

while True:
    try:
        print(input())
    except EOFError:
        break

'''
while 문이 true 일 때 루프를 돌리는 형식으로 4번 라인에서 볼 수 있듯이 EOFError만 예외처리를 통해 break할 수 있도록 하였습니다. 그 외에는 print(input()) 을 이용해 입력받는대로 바로 출력해주는 코드를 작성할 수 있습니다.
'''
        
