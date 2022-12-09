#프로그래머스
#두개 뽑아서 더하기

def solution(numbers):
    answer = []

    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            a = numbers[i]+numbers[j]
            if a not in answer:
                answer.append(a)
    answer = sorted(answer)
    return answer
