---
layout: post
title: "[프로그래머스] 캐시"
date: 2021-04-23 23:59 +0530
categories: 프로그래머스 KAKAO
---

알고리즘 풀기 106일차

:)

- # 캐시

>

## < 문제 >

지도개발팀에서 근무하는 제이지는 지도에서 도시 이름을 검색하면 해당 도시와 관련된 맛집 게시물들을 데이터베이스에서 읽어 보여주는 서비스를 개발하고 있다.

이 프로그램의 테스팅 업무를 담당하고 있는 어피치는 서비스를 오픈하기 전 각 로직에 대한 성능 측정을 수행하였는데, 제이지가 작성한 부분 중 데이터베이스에서 게시물을 가져오는 부분의 실행시간이 너무 오래 걸린다는 것을 알게 되었다.

어피치는 제이지에게 해당 로직을 개선하라고 닦달하기 시작하였고, 제이지는 DB 캐시를 적용하여 성능 개선을 시도하고 있지만 캐시 크기를 얼마로 해야 효율적인지 몰라 난감한 상황이다.

어피치에게 시달리는 제이지를 도와, DB 캐시를 적용할 때 캐시 크기에 따른 실행시간 측정 프로그램을 작성하시오.

## < 조건 >

캐시 교체 알고리즘은 LRU(Least Recently Used)를 사용한다.

cache hit일 경우 실행시간은 1이다.

cache miss일 경우 실행시간은 5이다.

## < 풀이 >

```python

from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cities = list(map(str.lower, cities))

    queue = deque([0 for i in range(cacheSize)])

    if cacheSize == 0:
        return len(cities)*5

    for city in cities:
        if city in queue:
            answer+=1
            queue.remove(city)
        else:
            answer+=5
            queue.popleft()
        queue.append(city)

    return answer

```

> ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]

테스트 케이스가 위와 같이 도시 명이 있는 배열이 들어온다.

대소문자 구분없이 들어오기에 다 소문자로 통일해주었다.

쌓이고 빠질 큐를 만들어주었다. 리스트로 하기엔 앞뒤로 들어오고 빠질 것이기에 효율이 더 좋은 deque를 사용해주었다.

해당 큐의 사이즈는 캐시 사이즈 만큼으로 만들어준다.

캐시 사이즈가 0, 즉 캐시 저장 못해둘 거면 다 그냥 5 곱해주고 리턴

반복문을 돌면서 캐시 저장된 도시라면 1만 더하고 해당 도시를 위치에서 빼준다. 그리고 다시 맨 위에 쌓는다. (최근에 쓴 거 위로가게)

만약에 캐시에 저장 안된 도시라면 5를 더하고 맨 왼쪽 캐시를 빼준다. (가장 오래 안불린 도시 - LRU알고리즘)

어쨌든 현재 도시를 append해줌으로써 가장 최근에 사용된 도시가 위로가고 popleft를 하면 가장 오래동안 참조안된 도시가 나가게 짰다.

---

맨처음에

```python

    for city in cities:
        if city in queue:
            answer+=1
        else:
            answer+=5
        queue.popleft()
        queue.append(city)

```

이렇게 짰는데 몇가지 케이스가 틀려서 왜지 생각했더니 LRU로 짜지 않고 그냥 FIFO인 알고리즘이다.
