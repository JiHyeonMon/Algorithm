#완주하지 못한 선수

def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    for i in range(0, len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            break
            
    if answer == '':
        answer = participant[len(completion)]
    return answer
