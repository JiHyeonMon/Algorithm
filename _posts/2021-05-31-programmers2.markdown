---
layout: post
title: "[프로그래머스] H-index"
date: 2021-05-31 23:01 +0530
categories: 프로그래머스 정렬
---

알고리즘 풀기 224일차

:)

- # H-index
  >

## < 문제 >

H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다. 어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다. 위키백과1에 따르면, H-Index는 다음과 같이 구합니다.

어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.

어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.

## < 제한사항 >

과학자가 발표한 논문의 수는 1편 이상 1,000편 이하입니다.

논문별 인용 횟수는 0회 이상 10,000회 이하입니다.

## < 풀이 >

```python

def solution(citations):
    answer = 0
    n = len(citations)
    citations.sort()

    for i in range(n):
        if citations[i] >= n-i:
            return n-i
    return 0

#     for i in range(n, -1, -1):
#         cnt = 0
#         if citations[0] > i:
#             return i

#         for j in range(n-1, -1, -1):
#             if citations[j]>=i:
#                 cnt += 1
#             else:
#                 break
#         if cnt>=i:
#             return i

```

위에 코드 + 아래 주석 모두 통과.

아래 코드 먼저 생각해서 풀었는데 다른 사람 풀이 중 괜찮은 것을 하나 들고와봤다.

우선 최대 값은 citations의 길이가 된다. ==> h번 이상 인용된 논문이 h편 이상

그래서 길이의 최대값부터 내려오면서 개수 비교하며 cnt 하는 방식으로 구했다. (사실 쉬운 문제 같아 보였는데 생각하는데 꽤나 골머리 썩힘)

통과는 했는데 이렇게 풀기 전에 틀렸던 풀이가 있는데 다른 사람 풀이를 보니 같은 생각으로 푼 풀이가 있어 가져와봤다.

그냥 citations 길이만큼 돌며 0~최대 길이까지 인덱스라 치면, 해당 인덱스가 가리키는 값이 해당 값 뒤로 남은 수들보다 같아지게 되는 순간이 최대다. (단 정렬을 해놔야 함.)

    [0, 1, 3, 5, 6]
    0부터 돌면서 3을 가리켰는데, 해당 3값 포함 뒤로 남은 수가 3일 때 최대값이 된다.
