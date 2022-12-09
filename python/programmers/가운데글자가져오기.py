#가운데 글자 가져오기

import math
def solution(s):
    answer = ''
    if len(s)%2==1:
        answer = s[math.floor(len(s)/2)]
    else:
        answer = s[len(s)//2-1]+s[len(s)//2]
    return answer
