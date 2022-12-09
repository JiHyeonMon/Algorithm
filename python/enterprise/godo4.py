#4
#핵심 소스코드의 설명을 주석으로 작성하면 평가에 큰 도움이 됩니다.
class Solution:
    def solution(self, cardNumber):
        n_cardNumber = list(map(int, cardNumber))
        total = 0
        if len(cardNumber)%2!=0: #홀수 개면
            for i in range(1, len(cardNumber), 2): #짝수자리 수 *2
                n_cardNumber[i]*=2
        else:
            for i in range(0, len(cardNumber), 2): #짝수 --> 홀수자리 수*2
                n_cardNumber[i]*=2
                
        #각 자리의 합이기때문에 한칸에 두자리 수가 들어갈 수도 있으니 일단 다시 str타입으로 바꿔준다.
        #리스트를 str으로 바꾸고 조인을 통해 한 문자열로 바꿔준다.
        s_cardNumber = ''.join(list(map(str, n_cardNumber)))
        
        #각 문자열 자리를 더해준다.
        for i in range(0,len(s_cardNumber)):
            total += int(s_cardNumber[i])
            
        #10의 배수인지 체크한다.
        if total % 10 ==0:
            return "VALID"
        else:
            return "INVALID"
