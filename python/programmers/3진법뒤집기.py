#3진법 뒤집기


def solution(m):
     multi = []
     answer = []
     i=0
     sum = 0
     while m>=3:
          if 3**i>m:
               multi.append(i-1)
               m -= 3**(i-1)
               i=0
          else:
               i+=1
               
     for i in range(m):multi.append(0)

     for i in range(max(multi), -1, -1):
          if i in multi:
               answer.append(multi.count(i))
          else:
               answer.append(0)
               
     answer = list(reversed(answer))

     for i in range(0, len(answer)):
          sum+=answer[len(answer)-i-1]*(3**i)

     print(sum)
     
solution(45)
