---
layout: post
title: "[프로그래머스] 부족한 금액 계산하기"
date: 2021-08-13 09:01
categories: 프로그래머스 위클리챌린지

---

알고리즘 풀기 235일차

3주만에 등장~

:)

- # 부족한 금액 계산하기


## < 문제 >

새로 생긴 놀이기구는 인기가 매우 많아 줄이 끊이질 않습니다. 이 놀이기구의 원래 이용료는 price원 인데, 놀이기구를 N 번 째 이용한다면 원래 이용료의 N배를 받기로 하였습니다. 

즉, 처음 이용료가 100이었다면 2번째에는 200, 3번째에는 300으로 요금이 인상됩니다.

놀이기구를 count번 타게 되면 현재 자신이 가지고 있는 금액에서 얼마가 모자라는지를 return 하도록 solution 함수를 완성하세요.

단, 금액이 부족하지 않으면 0을 return 하세요.

## < 제한사항 >

놀이기구의 이용료 price : 1 ≤ price ≤ 2,500, price는 자연수

처음 가지고 있던 금액 money : 1 ≤ money ≤ 1,000,000,000, money는 자연수

놀이기구의 이용 횟수 count : 1 ≤ count ≤ 2,500, count는 자연수

## < 풀이 >

```python

def solution(price, money, count):
    totalMoney = 0
    for i in range(count):
        totalMoney += price*(i+1)
    if totalMoney<=money:
        return 0
    return totalMoney-money

```

좌존쉼 상훼,,, 굉장 쉬운 문제 5번은 틀려 알고리즘 3주 공백 타격 씨게 맞았습니다. (바보냐,,)

솔직히 풀이도 필요없을 쉬운 문젠데 말이죠. 머쓱-

전 그냥 생각나는대로 정석? 방법으로 매번 price 가 count 지날 수록 커지니 totalMoney 변수로 만들어 매번 커지는 price 만큼 더해 만들어줍니다.

이후 리턴에 있어 부족하지 않다면 0, 부족하면 차액만큼 리턴하게 구현했습니다.

아래는 다른 사람 풀이.


```python

def solution(price, money, count):
    return max(0,price*(count+1)*count//2-money)
    
```


^_______________^

아주 깔끔 간결
나도 노력하자, 화이팅~ 

totalMoney = price*(count+1)*count//2

수학으로 푼 방식.

1~n 까지의 합  == n*(n+1)/2

근데 여기서 1씩 증가가 아니라 price 만큼 커지니 price 역시 곱해준다. 

