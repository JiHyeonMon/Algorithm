---
layout: post
title:  "프로그래머스 코딩테스트"
date:   2021-03-04 23:59 +0530
categories: python
---

알고리즘 풀기 80일차

:)

- #주식가격

# <문제 설명>

초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

# <제한사항>
prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
prices의 길이는 2 이상 100,000 이하입니다.


# <풀이>

```python

def solution(prices):
    answer = []
    init = len(prices)    
    
    for i in range(len(prices)):
        if prices[i] is min(prices[i:]):
            answer.append(len(prices)-(i+1))
            
        else:
            for j in range(i+1, len(prices)):
                if prices[i]>prices[j]:
                    answer.append(j-i)
                    break
        
    return answer

```

```python

def solution(prices):
    answer = []
    init = len(prices)
    
    i = 0
    while i<init:
            
        if prices[0] is min(prices):
            answer.append(len(prices)-1)
            prices.pop(0) 
        else:
            for j in range(1, len(prices)):
                if prices[0]>prices[j]:
                    answer.append(j)
                    prices.pop(0)
                    break
        i+=1

    return answer

```

위아래 모두 테스트케이스는 만족 - 그러나 모두 효율성 실패. 즉 시간초과가 난다.

이전 백준 문제 풀때도 시간초과가 제일 애먹었는데,,,

두 코드는 거의 같다. 

해당 자리 수가 최소값이면 (뒤로 주가가 내릴 리 없으니) 맨 뒤까지 초를 세주면 된다.

만약 최소가 아니라면 현 시점부터 언제 주가가 내리는지 반복문을 통해 찾게했다.

정답을 찾는데 문제는 없는 코드지만, 효율 바닥.

어떻게 고쳐야할까,,,,

(내일 찾아보도록 하자.)