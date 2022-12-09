#2908
#두 수가 주어졌을 때, 상수의 대답을 출력하는 프로그램을 작성하시오.

def reverse(a):
    return int(a[2]+a[1]+a[0])

a, b = input().split()

if reverse(a)>reverse(b):
    print(reverse(a))
else:
    print(reverse(b))

'''
a, b = input().split(' ')
a = a[::-1]
b = b[::-1]
if a > b:
    print(a)
else:
    print(b)
'''
