#10872
#0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

def fac(a):
    if a>1:
        return a * fac(a-1)
    else:
        return 1
    
a = int(input())

print(fac(a))
    
