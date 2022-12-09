#2675
#문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오.

total = int(input())
for i in range(0, total):
    sentence = ""
    num, a = input().split()
    for j in range(0 , len(a)):
        sentence += a[j]*int(num)
    print(sentence)
