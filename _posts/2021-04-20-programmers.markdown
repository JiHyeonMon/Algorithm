---
layout: post
title: "프로그래머스 코딩테스트"
date: 2021-04-20 23:59 +0530
categories: python
---

알고리즘 풀기 103일차

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

틀림 + 시간 초과

---

```python

import heapq
def solution(scoville, K):
    answer = 0
    num = []
    for i in scoville:
        heapq.heappush(num, i)

    while num[0]<K:
        if len(num)<2:
            return -1
        heapq.heappush(num, heapq.heappop(num)+heapq.heappop(num)*2)
        answer+=1

    return answer

```

deque를 정렬할 수 있을까 생각하다 heapq를 알게됐다.

자동으로 정렬이 되는 최대, 최소값을 찾기 쉬운, 우선순위 큐를 위해 만들어진 자료구조가 힙이라 한다.

그렇기에 heappush를 하면 자동으로 맞는 자리에 push가 되고 계산한 값을 그냥 넣고, pop으로 작은 수를 차례로 빼주면 해결이 됐다.

마지막 예외처리로 K보다 커지지 않는 경우 -1을 리턴하는 조건을 걸지 않으니 런타임에러가 발생했는데 하나 남았을 때도 K보다 작으면 -1을 반환하게 수정하니 잘 동작하였다.

또한 예외 처리를 아래와 같이 try-except을 이용해서 에러 발생시 -1로 리턴하며 끝나는 방식도 보며 다음에 써봐야겠다는 생각이 들었다.

```python

while heap[0] < k:
    try:
        heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) * 2))
    except IndexError:
        return -1
    ix_cnt += 1

```
