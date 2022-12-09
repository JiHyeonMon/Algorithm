#11720
#N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

a = int(input())
b = input()
sum = 0
for i in range(a):
    sum = sum + int(b[i])

print(sum)


'''
list1=[]

n=(input())
list1=list(map(int,input()))


print(sum(list1))
'''
