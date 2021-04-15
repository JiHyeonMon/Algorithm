---
layout: post
title: "프로그래머스 코딩테스트"
date: 2021-04-12 23:59 +0530
categories: python
---

알고리즘 풀기 99일차
알고리즘 풀기 100일차

:)

- # 가장 먼 노드

# < 문제 >

n개의 노드가 있는 그래프가 있습니다. 각 노드는 1부터 n까지 번호가 적혀있습니다. 1번 노드에서 가장 멀리 떨어진 노드의 갯수를 구하려고 합니다. 가장 멀리 떨어진 노드란 최단경로로 이동했을 때 간선의 개수가 가장 많은 노드들을 의미합니다.

노드의 개수 n, 간선에 대한 정보가 담긴 2차원 배열 vertex가 매개변수로 주어질 때, 1번 노드로부터 가장 멀리 떨어진 노드가 몇 개인지를 return 하도록 solution 함수를 작성해주세요.

![image](https://user-images.githubusercontent.com/50662636/114182936-3475da80-997e-11eb-96e6-6ebb1959405f.png)

# < 제한사항 >

노드의 개수 n은 2 이상 20,000 이하입니다.

간선은 양방향이며 총 1개 이상 50,000개 이하의 간선이 있습니다.

vertex 배열 각 행 [a, b]는 a번 노드와 b번 노드 사이에 간선이 있다는 의미입니다.

# < 풀이 >

```python

def solution(n, edge):
     answer = 0

     # 이중 배열의 안의 배열 정렬
     for i in range(len(edge)):
          edge[i] = sorted(edge[i])
     # 이중 배열의 바깥 배열 정렬
     edge = sorted(edge)

     # 엣지 개수 만큼 0 채운 배열 만듬
     num = [0 for i in range(n)]

     d = []
     for i in range(len(edge)):
          if edge[i][0] == 1:
               d[edge[i][1]] = 1

     for i in range(len(edge)):
          if d[edge[i][1]] != 0:
               continue
          else:
               d[edge[i][1]] = d[edge[i][0]]

     print(d)


     return answer

n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
solution(n, edge)

```

사실 아직 푸는 중.........

> 1 ) edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

> 2 ) 이중 배열 안의 정렬

> 2 ) edge = [[3, 6], [3, 4], [2, 3], [1, 3], [1, 2], [2, 4], [2, 5]]

> 3 ) 배열 정렬

> 3 ) edge = [[1, 2], [1, 3], [2, 3], [2, 4], [2, 5], [3, 4], [3, 6]]

여기서 n길이의 0으로 찬 배열을 만들어서 해당 노드에 가중치? 거리를 더해주려고 한다.

n = [ 0, 0, 0, 0, 0, 0]

[1, 2], [1, 3]이니 d에 2, 3번째 자리에 가중치 1

n = [0, 1, 1, 0, 0, 0]

이런 식으로 생각만~~~

---

```python

import collections

def solution(n, edge):
    answer = 0

    # 이중 배열의 안의 배열 정렬
    for i in range(len(edge)):
        edge[i] = sorted(edge[i])
    # 이중 배열의 바깥 배열 정렬
    edge = sorted(edge)

    # 시간 효율성 위해 deque로 구현
    edge = collections.deque(edge)

    # 엣지 개수 만큼 0 채운 배열 만듬
    num = [0] * n

    i = 0
    while edge:
        i+=1
        tmp = edge.popleft()
        if num[tmp[1]-1] == 0:
            num[tmp[1]-1] = num[tmp[0]-1] + 1
        else:
            continue

    return num.count(max(num))

n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
solution(n, edge)

```

두번째 시도

테스트는 통과, 그러나 안통과,,,,,,,,,,

해당 아래 예시는 통과한다,,,^^ 더 수정 필요

우선 위의 풀이에서 수정한게 정렬 후 Queue로 만들어 넣는다. 그래서 하나하나 앞에서부터 값을 빼면서 num에 거리를 계산해서 넣어준다.

---

```python

from collections import deque
def solution(n, edge):
     graph = [[] for _ in range(n)]

     # 그래프 연결 정보 초기화.
     for node, connect in edge:
          graph[node - 1].append(connect - 1)
          graph[connect - 1].append(node - 1)

     # visited로 노드 간의 길이를 카운트.
     visited = [0] + [-1] * (n - 1)

     # 첫 번째 시작 노드는 [1번 노드]
     q = deque([[0, 0]])

     while q:
          cur_node, dist = q.popleft()

          for next_node in graph[cur_node]:
               if visited[next_node] == -1:
                    q.append([next_node, dist + 1])
                    visited[next_node] = dist + 1

     # visited의 max값과 그것을 카운트 한것은 가장 먼 노드의 수.
     return visited.count(max(visited))

```

계속 100점이 안나와서 코드를 찾아보았다.

모든 사람의 코드가 다 같은 것은 아니었지만 그 중 제일 비슷해보이는 (거의 비슷하지만) 코드를 가져와봤다.

gragh라는 배열에 각 노드에 어떤 노드가 연결됐는지를 담아준다.

> [[2, 1], [2, 0, 3, 4], [5, 3, 1, 0], [2, 1], [1], [2]]

이런 식으로 담기게 된다.

visited배열에 이제 인덱스를 각 노드 번호로 1번 노드와의 거리를 담을 것이다.

그러고 gragh를 돌면서 다음 gragh값이 -1 즉 아직 거리 측정 안됐지만 연결된 노드라면 거리를 1 더해서 거리를 기록한다.

---

사실 아이디어 상으로 내 코드와 크게 다를 것 없는 것 같은데, 아닌가,,,,,,,,,,ㅎ,,,,
