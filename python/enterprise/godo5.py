#5
#핵심 소스코드의 설명을 주석으로 작성하면 평가에 큰 도움이 됩니다.
class Solution:
    def solution(self, votes):
        cnt = 0
        
        #votes의 최댓값을 후보0의 값과 계속 비교하며 후보0을 가장 높은 값으로 만들어준다.
        while max(votes)!=votes[0]:
            i = votes.index(max(votes))
            votes[i]-=1
            votes[0]+=1
            cnt+=1
        
        #그러나 가장 높은 값이라도 같은 값이 있을 수 있다.
        #후보0과 같은 값이 있다면(가장 높은 수), 후보0에게 한표 준다.
        for i in range(1, len(votes)):
            if votes[0]==votes[i]:
                votes[0]+=1
                votes[i]-=1
                cnt+=1
                continue
    
        return cnt
