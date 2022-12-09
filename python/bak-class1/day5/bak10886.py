#10886
#준희는 자기가 팀에서 귀여움을 담당하고 있다고 생각한다. 하지만 연수가 볼 때 그 의견은 뭔가 좀 잘못된 것 같았다. 그렇기에 설문조사를 하여 준희가 귀여운지 아닌지 알아보기로 했다.


cnt = 0

for i in range(int(input())):
     if int(input()) == 1:
          cnt+=1
     else:
          cnt-=1
if cnt>0:
     print("Junhee is cute!")
else:
     print("Junhee is not cute!")
