#2

#핵심 소스코드의 설명을 주석으로 작성하면 평가에 큰 도움이 됩니다.
class Solution:
     def solution(self, page, broken):
          number = [0,1,2,3,4,5,6,7,8,9]
          init = 100
          answer=[]
          s_page = str(page)
          for i in range(len(broken)):
               number[broken[i]]=-1
          print(number)

     
          for i in range(0,len(s_page)):
               if int(s_page[i])==str(init)[i]:
                    answer.append(str(init)[i])
               else:
                    if number[int(s_page[i])]!=-1:
                         answer.append(int(s_page[i]))
                    else:
                         for j in range(1, len(number)-1):
                              if number[int(s_page[i])-i] != -1:
                                   answer.append(int(s_page[i])-i)
                                   break

                              if number[int(s_page[i])+i] != -1:
                                   answer.append(int(s_page[i])+i)
                                   break
               
          return answer

page=143
broken=[1,4,5]
a = Solution()
print(a.solution(page,broken))
