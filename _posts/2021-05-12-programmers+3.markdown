---
layout: post
title: "[프로그래머스] 실패율"
date: 2021-05-12 23:59 +0530
categories: 프로그래머스
---

알고리즘 풀기 116일차

:)

- # 실패율

>

## < 문제 >

슈퍼 게임 개발자 오렐리는 큰 고민에 빠졌다. 그녀가 만든 프랜즈 오천성이 대성공을 거뒀지만, 요즘 신규 사용자의 수가 급감한 것이다. 원인은 신규 사용자와 기존 사용자 사이에 스테이지 차이가 너무 큰 것이 문제였다.

이 문제를 어떻게 할까 고민 한 그녀는 동적으로 게임 시간을 늘려서 난이도를 조절하기로 했다. 역시 슈퍼 개발자라 대부분의 로직은 쉽게 구현했지만, 실패율을 구하는 부분에서 위기에 빠지고 말았다. 오렐리를 위해 실패율을 구하는 코드를 완성하라.

실패율은 다음과 같이 정의한다.

    스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수

전체 스테이지의 개수 N, 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages가 매개변수로 주어질 때, 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return 하도록 solution 함수를 완성하라.

## < 제한 >

스테이지의 개수 N은 1 이상 500 이하의 자연수이다.

stages의 길이는 1 이상 200,000 이하이다.

stages에는 1 이상 N + 1 이하의 자연수가 담겨있다.

각 자연수는 사용자가 현재 도전 중인 스테이지의 번호를 나타낸다.

단, N + 1 은 마지막 스테이지(N 번째 스테이지) 까지 클리어 한 사용자를 나타낸다.

만약 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오도록 하면 된다.

스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의한다.

## < 풀이 >

```python
# 정답

def solution(N, stages):
    answer = []
    failure = []
    stages = sorted(stages)
    for i in range(1, N+1):
        # 런타임에러 = 해당 아래 조건 추가. 테케 1,6,7,9,13,11,24,25
        if stages.count(i) == 0:
            failure.append([i, 0])
            continue
        p=0
        for j in range(len(stages)):
            if stages[j] >= i:
                p+=1
        failure.append([i, stages.count(i)/p])
    failure = sorted(failure, key = lambda x:x[1], reverse=True)
    answer = [i[0] for i in failure]
    return answer



# 아래는 이전에 시간초과 난 코드
'''
def solution(N, stages):
    answer = []
    n = {}
    for i in range(0,N):
        bigger = 0
        for j in range(0, len(stages)):
            if stages[j] >= i+1:
                bigger += 1
        if stages.count(i+1)==0:
            n[i+1]=0
        else:
            n[i+1]= stages.count(i+1)/bigger

    n = sorted(n.items(), key=lambda t : t[1], reverse = True)

    for i in range(0,N):
        answer.append(n[i][0])
    return answer
'''


# 아래 주석의 요인을 해결해주니 문제 해결
def solution(N, stages):
    answer = []
    n = {}
    # range의 범위 값을 1부터 N+1로 하여 반복문 내에서 계산을 줄인다.
    for i in range(1, N+1):
        # 1. 반복문 빠져나갈 예외조건 먼저 처리하여 쓸데없는 반복 줄임
        if stages.count(i)==0:
            n[i]=0
            continue
        else:
            bigger = 0
            for j in range(len(stages)):
                if stages[j] >= i:
                    bigger += 1

            n[i]= stages.count(i)/bigger

    n = sorted(n.items(), key=lambda t : t[1], reverse = True)

    for i in range(0,N):
        answer.append(n[i][0])
    return answer

```
