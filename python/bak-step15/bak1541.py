#1541
#잃어버린 괄호

expression = input().split('-')
answer = 0
for i in expression[0].split('+'):
     answer += int(i)
for i in expression[1:]:
     answer-=sum(list(map(int, i.split('+'))))
     
print(answer)
