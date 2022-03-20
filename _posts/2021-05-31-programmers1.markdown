---
layout: post
title: "[프로그래머스] 다리를 지나는 트럭"
date: 2021-05-31 23:01 +0530
categories: 프로그래머스 정렬 큐
---

알고리즘 풀기 224일차

:)

- # 다리를 지나는 트럭
  >

## < 문제 >

트럭 여러 대가 강을 가로지르는 일 차선 다리를 정해진 순으로 건너려 합니다. 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다. 트럭은 1초에 1만큼 움직이며, 다리 길이는 bridge_length이고 다리는 무게 weight까지 견딥니다.

※ 트럭이 다리에 완전히 오르지 않은 경우, 이 트럭의 무게는 고려하지 않습니다.

예를 들어, 길이가 2이고 10kg 무게를 견디는 다리가 있습니다. 무게가 [7, 4, 5, 6]kg인 트럭이 순서대로 최단 시간 안에 다리를 건너려면 다음과 같이 건너야 합니다.

|경과 시간| 다리를 지난 트럭| 다리를 건너는 트럭 대기 트럭|
|0| []| []| [7,4,5,6]|
|1~2| []| [7]| [4,5,6]|
|3| [7]| [4]| [5,6]|
|4| [7]| [4,5]| [6]|
|5| [7,4]| [5]| [6]|
|6~7| [7,4,5]| [6]| []|
|8| [7,4,5,6]| []| []|

따라서, 모든 트럭이 다리를 지나려면 최소 8초가 걸립니다.

solution 함수의 매개변수로 다리 길이 bridge_length, 다리가 견딜 수 있는 무게 weight, 트럭별 무게 truck_weights가 주어집니다. 이때 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 return 하도록 solution 함수를 완성하세요.

## < 제한사항 >

bridge_length는 1 이상 10,000 이하입니다.

weight는 1 이상 10,000 이하입니다.

truck_weights의 길이는 1 이상 10,000 이하입니다.

모든 트럭의 무게는 1 이상 weight 이하입니다.

## < 풀이 >

```python

from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 0
    truck_weights = deque(truck_weights)
    bridge = deque([0 for i in range(bridge_length)])
    while truck_weights:
        time+=1
        bridge.popleft()
        if sum(bridge) + truck_weights[0]<=weight:
            bridge.append(truck_weights.popleft())
        else:
            bridge.append(0)

    return time+bridge_length

```

정말 큐를 이용해서 앞뒤로 넣고 뺄 수 있게 하며 구현했다.

우선 truck_weights은 앞에서부터 뺄테니 deque로 바꿔서 효율성을 높인다.

그리고 bridge 큐를 하나 만든다. 이 때 길이를 다리 길이에 맞춰준다.

그리고 시간 1초씩 지나며 bridge 하나 빼고 하나 넣고를 반복한다.

다리 위에 무게를 비교해서 weight을 안넘으면 새로운 트럭을 올리고 아니면 0을 그냥 넣어준다.

그렇게 트럭을 다 올리고 truck_weights이 비면 ---> 마지막 트럭이 다리 위로 올라간 순간이다.

그래서 기존 time에 마지막 트럭이 time이 될 다리 길이를 더해준 값을 리턴한다.
