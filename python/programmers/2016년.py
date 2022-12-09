#2016년
def solution(a, b):
    sum = 0
    m = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    d = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    for i in range(a-1):
        sum += m[i]
    
    answer = d[(sum+b-1)%7]
    return answer
