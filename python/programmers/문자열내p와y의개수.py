#문자열 내 p와 y의 개수

def solution(s):
    answer = True
    pc, yc = 0,0
    s = s.upper()
    for i in range(len(s)):
        if s[i] == 'P':
            pc+=1
        if s[i] == 'Y':
            yc+=1
    if pc==yc :
        answer = True
    else:
        answer = False
    return answer
