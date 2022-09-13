---
layout: post
title: "[프로그래머스] 위장 (수정)"
date: 2021-04-06 23:59 +0530
categories: 프로그래머스
---

알고리즘 풀기 95일차

알고리즘 풀기 96일차

:)

- # 위장

## < 문제 >

계속되는 폭우로 일부 지역이 물에 잠겼습니다. 물에 잠기지 않은 지역을 통해 학교를 가려고 합니다. 집에서 학교까지 가는 길은 m x n 크기의 격자모양으로 나타낼 수 있습니다.

아래 그림은 m = 4, n = 3 인 경우입니다.

![image](https://user-images.githubusercontent.com/50662636/113728468-19625b00-9731-11eb-961e-0b5d859c9137.png)

가장 왼쪽 위, 즉 집이 있는 곳의 좌표는 (1, 1)로 나타내고 가장 오른쪽 아래, 즉 학교가 있는 곳의 좌표는 (m, n)으로 나타냅니다.

격자의 크기 m, n과 물이 잠긴 지역의 좌표를 담은 2차원 배열 puddles이 매개변수로 주어집니다. 오른쪽과 아래쪽으로만 움직여 집에서 학교까지 갈 수 있는 최단경로의 개수를 1,000,000,007로 나눈 나머지를 return 하도록 solution 함수를 작성해주세요.

## < 제한사항 >

격자의 크기 m, n은 1 이상 100 이하인 자연수입니다.

m과 n이 모두 1인 경우는 입력으로 주어지지 않습니다.

물에 잠긴 지역은 0개 이상 10개 이하입니다.

집과 학교가 물에 잠긴 경우는 입력으로 주어지지 않습니다.

## < 풀이 >

```python

d = []
def calculate(i, j, k, puddles, m, n):
    if [i+1, j] == [m, n] or [i, j+1] == [m, n]:
        d.append(k+1)
        return

    if [i+1, j] == [m, n] or [i, j+1] == [m, n]:
        d.append(k+1)
        return

    if [i+1, j] not in puddles or [i, j+1] not in puddles:
        k+=1
        calculate(i+1, j, k, puddles, m, n)
        calculate(i, j+1, k, puddles, m, n)

def solution(m, n, puddles):
    answer = 0
    k = 0
    i, j = 1, 1
    calculate(i, j, k, puddles, m, n)
    return answer

m = 4
n = 3
puddles = [[2,2]]
solution(m, n, puddles)

```

사실,,,아직 푸는 중임....

## < 풀이 2 >

```python

def solution(m, n, puddles):
    d = [[0 for i in range(m+1)] for i in range(n+1)]
    d[1][1] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue

            if [j, i] in puddles:
                d[i][j] = 0

            else:
                d[i][j] = (d[i-1][j]+d[i][j-1]) % (1000000007)

    return d[n][m]

'''
m   n   puddles   return
4   3   [[2, 2]]
'''

```

계속 틀렸다 떴는데 장애물 확인하는 과정에서 i, j 순서 바꿔서 함. 가로로 가는게 j 인데 자연스레 i, j로 적어서 찾느라 살짝 헤맸다.

> if [j, i] in puddles:
