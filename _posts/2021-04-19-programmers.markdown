---
layout: post
title: "프로그래머스 코딩테스트"
date: 2021-04-19 23:59 +0530
categories: python
---

알고리즘 풀기 102일차

:)

- # 더 맵게

## < 문제 >

어떤 정수들이 있습니다. 이 정수들의 절댓값을 차례대로 담은 정수 배열 absolutes와 이 정수들의 부호를 차례대로 담은 불리언 배열 signs가 매개변수로 주어집니다. 실제 정수들의 합을 구하여 return 하도록 solution 함수를 완성해주세요.매운 것을 좋아하는 Leo는 모든 음식의 스코빌 지수를 K 이상으로 만들고 싶습니다. 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 Leo는 스코빌 지수가 가장 낮은 두 개의 음식을 아래와 같이 특별한 방법으로 섞어 새로운 음식을 만듭니다.

> 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 \* 2)

Leo는 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞습니다.

Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때, 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return 하도록 solution 함수를 작성해주세요.

## < 제한사항 >

scoville의 길이는 2 이상 1,000,000 이하입니다.

K는 0 이상 1,000,000,000 이하입니다.

scoville의 원소는 각각 0 이상 1,000,000 이하입니다.

모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.

## < 풀이 >

```python

#틀림 ing~~~~

def solution(scoville, K):
    answer = 0
    k = 0
    TF = False
    for i in range(len(scoville)-1):
        scoville = sorted(scoville)
        if scoville[i]<K:
            scoville[i+1] = scoville[i] + scoville[i+1]*2
            answer+=1
        else:
            TF = True
            break

    if TF:
        return answer
    else:
        return -1

```

오늘의 쉬운 문제. 그러나 틀림.

처음에 deque로 정의하여 popleft() 두개를 하여 계산했는데 또 문제를 보니 해당 값을 빼서 게산만 하는게 아니라 도로 집어넣어 다음 계산을 진행한다.

그래서 appendleft()를 하자니 다음 순서의 최소값이 아닐 가능성이 있다. (기존에 무조건 popleft로 빼오니 정렬이 돼야하는 상태)

그렇지만 deque에서는 sort를 지원하지 않는다.

그래서 다시 배열로 돌아왔다. 그러나 역시 예상대로 시간초과 문제.

해당 문제 카테고리가 힙(Heap)인 만큼 큐를 써서 풀어야할 것 같다.
