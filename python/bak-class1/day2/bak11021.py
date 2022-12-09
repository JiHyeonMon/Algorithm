#11021
#두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

num = int(input())

for i in range(1, num+1):
    a, b = input().split()
    print("Case #{}: {}".format(i, int(a)+int(b)) )

