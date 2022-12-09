#2018 KAKAO BLIND RECRUITING
#다트게임

def solution(dartResult):
    score = []
    n = ''
    for i in dartResult:
        if i.isnumeric():
            n += i
        elif i == 'S':
            score.append(int(n) ** 1)
            n = ''
        elif i == 'D':
            score.append(int(n) ** 2)
            n = ''
        elif i == 'T':
            score.append(int(n) ** 3)
            n = ''
        elif i == '*':
            if len(score) > 1:
                score[-2] *= 2
            score[-1] *= 2
        elif i == '#':
            score[-1] *= -1
    return sum(score)

dartResult = "1S*2T*3S"
print(solution(dartResult))
