#1712
#손익분기점

sta, exp, pri = map(int, input().split())
if pri<=exp: print(-1)
else:print(sta//(pri-exp)+1)




'''
sta, exp, pri = map(int, input().split())
answer = 1
while sta+(exp*answer)>pri*answer:
     answer += 1
print(answer+1)
'''

'''
sta+(exp*answer)<pri*answer
sta<(pri-exp)answer
sta/(pri-exp)<answer
를 만족하는 최소의 answer값을 찾아야함 


==>

sta, exp, pri = map(int, input().split())
print(sta//(pri-exp)+1)

'''

'''
첫 번째 줄에 손익분기점 즉 최초로 이익이 발생하는 판매량을 출력한다. 손익분기점이 존재하지 않으면 -1을 출력한다.

'''
