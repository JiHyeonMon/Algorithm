---
layout: post
title: "[프로그래머스] 주식가격"
date: 2021-06-01 23:01 +0530
categories: 프로그래머스 스택/큐
---

알고리즘 풀기 225일차

:)

- # 주식가격
  >

## < 문제 >

초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

## < 제한사항 >

prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.

prices의 길이는 2 이상 100,000 이하입니다.

## < 풀이 >

```python

def solution(prices):
    answer = [i for i in range(len(prices)-1, -1, -1)]

    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] > prices[j]:
                answer[i] = j-i
                break

    return answer

```

이전에 풀어둔 풀이가 있는데 틀렸으니 그대로겠지? 그대로 초기화하고 다시 푸니 5분만에 풀어버린 문제...(과연 전에 어떻게 짜둔거야,,,궁금할 정도)

일단 default로 answer에 최적의 시간? 모든 값이 떨어지지 않는 것을 기준으로 값을 넣어두고 시작한다. (아닐 경우 if 문 나와서 조건 처리 한번 더 필요)

각 price마다 확인하는데 뒤로 한 칸씩 가며 큰 지, 작은 지 비교한다.

뒤에 작은 수가 있다면 바로 break하고 몇 초가 됐는지 값을 갱신해주면 끝.
