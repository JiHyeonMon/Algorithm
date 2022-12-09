#15596
#정수 n개가 주어졌을 때, n개의 합을 구하는 함수를 작성하시오.

def solve(a):
    sum = 0
    for i in range(0, len(a)):
        sum += a[i]
    return print(sum)

k = [1,2,3,4,5,6,7,8,9,10]
solve(k)
