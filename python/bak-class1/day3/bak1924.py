#1924
#오늘은 2007년 1월 1일 월요일이다. 그렇다면 2007년 x월 y일은 무슨 요일일까? 이를 알아내는 프로그램을 작성하시오.

def day(x):
    return {1: 'MON', 2: 'TUE', 3: 'WED', 4: 'THU', 5:'FRI', 6:'SAT', 0:'SUN'}[x]

m, d = map(int, input().split())

list_m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if m > 1:
    for i in range(0, m-1):
        d += list_m[i]
    d%=7
else:
    d%=7

print(day(d))
