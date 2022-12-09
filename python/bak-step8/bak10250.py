#10250
# 설문조사 결과 대로 호텔 정문으로부터 걷는 거리가 가장 짧도록 방을 배정하는 프로그램을 작성하고자 한다.

case = int(input())

for i in range(case):
    h, w, num = map(int, input().split())
    mw = num//h+1
    floor = num%h
    if floor==0:
        mw-=1
        floor=h
    print(floor*100+mw)
