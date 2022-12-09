#4344
#대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.

size = int(input())
total = []
for i in range(0, size):
    case = []
    high = 0
    case = list(map(int, input().split()))
    avg = (sum(case)-case[0])/case[0]
    for j in range(1, case[0]+1):
        if(case[j]>avg):
            high += 1
    before = high/(len(case)-1)*100
    total.append('%0.3f' % before)

for i in range(0, len(total)):
    print('{}{}'.format(total[i],'%'))
