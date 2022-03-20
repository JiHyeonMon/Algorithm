---
layout: post
title: "[프로그래머스] 이중우선순위큐"
date: 2021-06-08 23:01 +0530
categories: 프로그래머스 힙
---

알고리즘 풀기 227일차

:)

- # 이중우선순위큐
  >

## < 문제 >

이중 우선순위 큐는 다음 연산을 할 수 있는 자료구조를 말합니다.

|명령어| 수신 탑(높이)|
|I 숫자| 큐에 주어진 숫자를 삽입합니다.|
|D 1| 큐에서 최댓값을 삭제합니다.|
|D -1| 큐에서 최솟값을 삭제합니다.|

이중 우선순위 큐가 할 연산 operations가 매개변수로 주어질 때, 모든 연산을 처리한 후 큐가 비어있으면 [0,0] 비어있지 않으면 [최댓값, 최솟값]을 return 하도록 solution 함수를 구현해주세요.

## < 제한사항 >

operations는 길이가 1 이상 1,000,000 이하인 문자열 배열입니다.

operations의 원소는 큐가 수행할 연산을 나타냅니다.

원소는 “명령어 데이터” 형식으로 주어집니다.- 최댓값/최솟값을 삭제하는 연산에서 최댓값/최솟값이 둘 이상인 경우, 하나만 삭제합니다.

빈 큐에 데이터를 삭제하라는 연산이 주어질 경우, 해당 연산은 무시합니다.

## < 풀이 >

```python

import heapq

def solution(operations):
    heap = []
    for i in range(len(operations)):
        if operations[i][0] == 'I':
            heapq.heappush(heap, int(operations[i][2:]))
        elif operations[i] == "D -1":
            if not heap:
                continue
            heapq.heappop(heap)
        elif operations[i] == "D 1":
            if not heap:
                continue
            heap.pop()
        else:
            heap.pop(heap.index(operations[i][2:]))

    if not heap:
        return [0,0]

    else:
        return [max(heap), min(heap)]

```

힙 정렬로 정렬하여 순차적으로 정렬해주는 python의 heapq를 사용하였다.

우선 I면 숫자를 넣는다. (자동 정렬)

D면 우선 비어있는지 확인하고 최대값을 뺀다면 정렬되어 있으니까 그냥 pop을 써서 제일 뒤에를 빼준다.

최소값을 뺀다면 그냥 pop(0)을 하면 다시 정렬 --> heapq를 써서 heappop으로 최소값을 빼준다.

그 외의 빼는 경우는 일반적인 pop으로 해당 값의 index를 찾아 빼준다.

이렇게 진행했을 때 남은 게 없으면 [0,0]을 반환하고 아니라면 [최대, 최소]로 반환한다.
