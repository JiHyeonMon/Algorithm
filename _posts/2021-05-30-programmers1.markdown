---
layout: post
title: "[프로그래머스] 구명보트"
date: 2021-05-30 17:54 +0530
categories: 프로그래머스 탐욕법
---

알고리즘 풀기 223일차

:)

- # 구명보트
  >

## < 문제 >

무인도에 갇힌 사람들을 구명보트를 이용하여 구출하려고 합니다. 구명보트는 작아서 한 번에 최대 2명씩 밖에 탈 수 없고, 무게 제한도 있습니다.

예를 들어, 사람들의 몸무게가 [70kg, 50kg, 80kg, 50kg]이고 구명보트의 무게 제한이 100kg이라면 2번째 사람과 4번째 사람은 같이 탈 수 있지만 1번째 사람과 3번째 사람의 무게의 합은 150kg이므로 구명보트의 무게 제한을 초과하여 같이 탈 수 없습니다.

구명보트를 최대한 적게 사용하여 모든 사람을 구출하려고 합니다.

사람들의 몸무게를 담은 배열 people과 구명보트의 무게 제한 limit가 매개변수로 주어질 때, 모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값을 return 하도록 solution 함수를 작성해주세요.

## < 제한사항 >

무인도에 갇힌 사람은 1명 이상 50,000명 이하입니다.

각 사람의 몸무게는 40kg 이상 240kg 이하입니다.

구명보트의 무게 제한은 40kg 이상 240kg 이하입니다.

구명보트의 무게 제한은 항상 사람들의 몸무게 중 최댓값보다 크게 주어지므로 사람들을 구출할 수 없는 경우는 없습니다.

## < 풀이 >

```python

from collections import deque
def solution(people, limit):
    answer = 0
    people = deque(sorted(people, reverse = True))

    while len(people)>1:
        if people[0]+people[-1]<=limit:
            people.pop()
            people.popleft()
        else:
            people.popleft()
        answer+=1

    if people:
        return answer+1
    else:
        return answer

```

일단 최대로 태울 수 있는 것도 두 명이기에 무거운 사람, 가벼운 사람 이렇게 짝짓는게 이득이다.

물론 가장 가벼운 사람과 가장 무거운 사람을 짝지었을 때, limit보다 커지면 무거운 사람 혼자밖에 못타는 것이기에 배열을 정렬한 뒤 맨 앞과 맨 뒤를 더해서 비교했다.

가장 가벼운 사람과 무거운 사람 합이 limit보다 작다면 둘을 빼고 answer+1

limit보다 크면 무거운 사람 혼자 나가고 answer+1

그러고 people에 혼자 남으면 한번 더 보내기에 answer+1, 다 비웠으면 return answer해준다.

무게 무거운 사람, 가벼운 사람 알기 위해 정렬 필요했고, 그 결과 앞뒤로 빼줘야하기에 일반 리스트(스택)으로 생각안하고 deque를 써서 앞에서 뺄 때도 효율을 높였다.
