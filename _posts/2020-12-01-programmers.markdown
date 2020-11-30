---
layout: post
title:  "프로그래머스 코딩테스트 문제9"
date:   2020-12-01 03:45 +0530
categories: python
---

알고리즘 풀기 30일차

:)


- #주식가격

초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

```python

def solution(prices):
    answer = []
    for i in range(len(prices)-1):
        if prices[i]>prices[i+1]:
            answer.append(prices[i]-prices[i+1])
        else:
            answer.append(len(prices)-(i+1))
    answer.append(0)
    return answer

```

아직 풀다 만 문제라 할 수 있다. 테스트케이스는 통과했지만, 100점은 아니다,,,
하아 또 할일하다보니 너무 졸려서 반성문을 생각하다,,,,,,,,,ㅋㅋㅋ큐ㅠㅠㅠㅠㅠ 프로그래머스 들어갔는데 역시나 어려워진 2단게에 몇문제 읽다가 풀었는데, 아직 수정이 필요하다,,,,