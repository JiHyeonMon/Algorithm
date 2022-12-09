#2019 카카오 블라인드 채용 문제
#실패율

def solution(N, stages):
     answer = []
     n = {}
     for i in range(0,N):
          bigger = 0
          for j in range(0, len(stages)):
               if stages[j] >= i+1:
                    bigger += 1
          if stages.count(i+1)==0:
               n[i+1]=0
          else:
               n[i+1]= stages.count(i+1)/bigger

               

     n = sorted(n.items(), key=lambda t : t[1], reverse = True)

     for i in range(0,N):
          answer.append(n[i][0])
     return answer

N = 4
stages = [2,1,3,2,1]
print(solution(N, stages))
