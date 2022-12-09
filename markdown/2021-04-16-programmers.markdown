---
layout: post
title: "[프로그래머스] 음양 더하기"
date: 2021-04-16 23:59 +0530
categories: 프로그래머스
---

알고리즘 풀기 101일차

:)

- # 음양 더하기

## < 문제 >

어떤 정수들이 있습니다. 이 정수들의 절댓값을 차례대로 담은 정수 배열 absolutes와 이 정수들의 부호를 차례대로 담은 불리언 배열 signs가 매개변수로 주어집니다. 실제 정수들의 합을 구하여 return 하도록 solution 함수를 완성해주세요.

## < 제한사항 >

absolutes의 길이는 1 이상 1,000 이하입니다.

absolutes의 모든 수는 각각 1 이상 1,000 이하입니다.

signs의 길이는 absolutes의 길이와 같습니다.

signs[i] 가 참이면 absolutes[i] 의 실제 정수가 양수임을, 그렇지 않으면 음수임을 의미합니다.

## < 풀이 >

```python

def solution(absolutes, signs):
    answer = 123456789

    for i in range(len(signs)):
        if not signs[i]:
            absolutes[i] = -absolutes[i]

    return sum(absolutes)

```

오늘의 쉬운 문제.

signs의 인덱스에 false면 음수니까 같은 인덱스의 absolutes의 값을 음수로 바꿔주고 해당 absolues의 합을 출력.
