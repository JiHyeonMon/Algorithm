---
layout: post
title: "[프로그래머스] 약수의 개수와 덧셈"
date: 2021-05-17 23:33 +0530
categories: 프로그래머스, 월간코드챌린지2
---

알고리즘 풀기 118일차

:)

- # 약수의 개수와 덧셈
  >

## < 문제 >

두 정수 left와 right가 매개변수로 주어집니다.

left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.

## < 풀이 >

```python

import math
def divisor(num):
    d = []
    for i in range(1, int(math.sqrt(num))+1):
        if num%i == 0:
            d.append(i)
            d.append(num//i)
    if len(set(d))%2 ==0:
        return True
    else:
        return False

def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if divisor(i):
            answer+=i
        else:
            answer-=i
    return answer

```

오랜만에 푸는 문제,,,

약수 구하는 함수를 따로 두고 반복문내 호출하며 구했다.

약수 구하는 반복문을 제곱근+1까지 구하는데 이러면 num이 16일 경우 4가 두번 들어간다.

그래서 set을 통해 중복을 제거한 개수를 판단한다.

아래는 다른 사람 코드인데 깔끔,,,,,,,,,,,

나도 풀이보며 해당 풀이를 이해했다.ㅋㅋㅋㅋㅋㅋㅋㅋ(?)

암튼 가운데 수가 제곱수면 당연 홀수. 자기\*자기니까

그렇다...

```python

def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer

```
