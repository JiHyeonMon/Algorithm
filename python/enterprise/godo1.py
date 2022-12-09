#nhn godo

#핵심 소스코드의 설명을 주석으로 작성하면 평가에 큰 도움이 됩니다.
def solution(goods):
     goods = sorted(goods)

     if sum(goods)<50:
          return sum(goods)
     
     if goods[0]>=50:
          return sum(goods)-30
          
     if goods[0]+goods[1]>=50 and goods[1]<50 and goods[2]>50:
          return sum(goods)-20
     else:
          return sum(goods)-10

class Solution:
     def solution(self, goods):
          goods = sorted(self._goods)
          if sum(goods)<50:
               return sum(goods)

          if goods[0]>=50:
               return sum(goods)-30
          if goods[0]+goods[1]>=50 and goods[1]<50 and goods[2]>50:
               return sum(goods)-20
          else:
               return sum(goods)-10

class Solution:
    def solution(self, goods):
        return 0
     
goods = [46,62,9]
print(solution(goods))

a = Solution(goods)
print(a.solution())
