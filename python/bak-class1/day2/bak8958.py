#8958
#OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.

size = int(input())
score = []

for i in range(0, size):
    problem = input()
    add_sum = 0
    sum = 0
    for j in range(0, len(problem)):
        if problem[j]=='O':
            add_sum += 1
        else:
            add_sum = 0
        sum +=add_sum
    score.append(sum)
    
for i in range(0, len(score)):
    print(score[i])
