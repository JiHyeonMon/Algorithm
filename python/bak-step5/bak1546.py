#1546
#세준이는 기말고사를 망쳤다. 세준이는 점수를 조작해서 집에 가져가기로 했다. 일단 세준이는 자기 점수 중에 최댓값을 골랐다. 이 값을 M이라고 한다. 그리고 나서 모든 점수를 점수/M*100으로 고쳤다.

size = int(input())

score = list(map(int, input().split()))
score.sort()

sum = 0

for i in range(0, size):
    score[i] = score[i]/score[size-1]*100
    sum += score[i]
print(sum/size)
