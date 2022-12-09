#나누어 떨이지는 숫자 배열

def solution(arr, divisor):
    answer = []
    for i in range(len(arr)):
        if arr[i]%divisor==0:
            answer.append(arr[i])
    
    if answer:
        answer = sorted(answer)
    else:
        answer.append(-1)
    return answer
