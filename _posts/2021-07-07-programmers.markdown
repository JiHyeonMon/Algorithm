---
layout: post
title: "[프로그래머스] 튜플"
date: 2021-07-07 23:01 +0530
categories: 프로그래머스 2019카카오개발자겨울인턴십
---

알고리즘 풀기 229일차

:)

- # 튜플
  >

## < 문제 >

셀수있는 수량의 순서있는 열거 또는 어떤 순서를 따르는 요소들의 모음을 튜플(tuple)이라고 합니다. n개의 요소를 가진 튜플을 n-튜플(n-tuple)이라고 하며, 다음과 같이 표현할 수 있습니다.

    (a1, a2, a3, ..., an)

튜플은 다음과 같은 성질을 가지고 있습니다.

- 중복된 원소가 있을 수 있습니다. ex : (2, 3, 1, 2)
- 원소에 정해진 순서가 있으며, 원소의 순서가 다르면 서로 다른 튜플입니다. ex : (1, 2, 3) ≠ (1, 3, 2)
- 튜플의 원소 개수는 유한합니다.

원소의 개수가 n개이고, 중복되는 원소가 없는 튜플 (a1, a2, a3, ..., an)이 주어질 때(단, a1, a2, ..., an은 자연수), 이는 다음과 같이 집합 기호 '{', '}'를 이용해 표현할 수 있습니다.

    {{a1}, {a1, a2}, {a1, a2, a3}, {a1, a2, a3, a4}, ... {a1, a2, a3, a4, ..., an}}

예를 들어 튜플이 (2, 1, 3, 4)인 경우 이는

    {{2}, {2, 1}, {2, 1, 3}, {2, 1, 3, 4}}

와 같이 표현할 수 있습니다. 이때, 집합은 원소의 순서가 바뀌어도 상관없으므로

    {{2}, {2, 1}, {2, 1, 3}, {2, 1, 3, 4}}
    {{2, 1, 3, 4}, {2}, {2, 1, 3}, {2, 1}}
    {{1, 2, 3}, {2, 1}, {1, 2, 4, 3}, {2}}

는 모두 같은 튜플 (2, 1, 3, 4)를 나타냅니다.

특정 튜플을 표현하는 집합이 담긴 문자열 s가 매개변수로 주어질 때, s가 표현하는 튜플을 배열에 담아 return 하도록 solution 함수를 완성해주세요.

## < 풀이 >

```python

from collections import deque
def solution(s):
    answer = []
    s = list(map(str, s[2:].split('},{')))
    #	['2', '2,1', '2,1,3', '2,1,3,4}}']

    s[-1] = s[-1][:-2]
    s = sorted(s, key=lambda x : len(x))
    # 	['2', '2,1', '2,1,3', '2,1,3,4']

    answer.append(int(s.pop(0)))

    for i in range(len(s)):
        s[i] = list(map(int, s[i].split(',')))
        # [,, [2, 1], [2, 1, 3], [2, 1, 3, 4]]

    s = deque(s)

    while s:
        tmp = s.popleft()
        for i in range(len(answer)):
            tmp.pop(tmp.index(answer[i]))
        answer += tmp

    return answer

```

이전에 풀다 만 문제 다시 풀었다.

(짠 코드에서 수정해버려서 온전히 이전 코드가 뭔지 알기 어렵지만 하단 주석 부분이 이전 코드의 일부)

이전에는 아마 2134면 2134 이렇게 나오고 순차적으로 빼는 식으로 짠 듯 한데 (오래돼 기억이 가물,,) 이 경우 문제가 2와 2가 들어간 여러 숫자가 있을 경우 구분이 어렵다는거다.

그래서 [2,1,3,4] 이렇게 배열로 따로 해서 생각해야 한다.

그래서 우선 숫자로 배열 만드는 과정이 필요했다.

주어진 입력이 {{1}, {1,2}} 이런 스트링 형식이어서 스트링으로 괄호를 자른다.

괄호를 자르고 길이 순으로 정렬한다.

첫번째에는 그럼 당연히 한자리 == 시작이 될테니 int로 바꿔 answer에 넣어주고 시작한다.

이후 '2,1,3,4' 이런 스트링을 콤마 기준 잘라 int형의 배열에 넣어 [2,1,3,4]로 만든다.

그리고 앞에서 부터 빼서 검사할 것이기에 deque로 변환하여 popleft를 사용한다.

하나하나 빼서 answer에 들어간 값인지 확인하며 answer에 있는 값이면 뺀다.

answer에 없는 값 == 하나만 남는다. (리스트)

그래서 answer에 추가해준다. 남는 값이 리스트 형태이기에 append가 아닌 +로 이어준다.

```python

from collections import deque
def solution(s):
    answer = []
    s = list(map(str, s[2:].split('},{')))
    #	['2', '2,1', '2,1,3', '2,1,3,4}}']

    s[-1] = s[-1][:-2]
    s = sorted(s, key=lambda x : len(x))
    # 	['2', '2,1', '2,1,3', '2,1,3,4']

    answer.append(int(s.pop(0)))

    for i in range(len(s)):
        s[i] = list(map(int, s[i].split(',')))
        # [,, [2, 1], [2, 1, 3], [2, 1, 3, 4]]

    s = deque(s)
    # print(answer)

    while s:
        tmp = s.popleft()
        for i in range(len(answer)):
            tmp.pop(tmp.index(answer[i]))
        # print(tmp)
        answer += tmp


    # for i in range(len(s)):
    #     s[i].pop(s[i].index(answer[-1]))
#     answer.append(int(s[0]))
#     print(s)
#     for i in range(1, len(s)):
#         tmp =

#         for j in range(len(answer)):
#             if answer[j] in tmp:
#                 tmp.pop(tmp.index(answer[j]))
#         answer.append(int(tmp))
#         print(answer)

#     print(answer)

#     if len(s) == 1:
#         return int(s[0])

#     for i in range(len(s)):
#         s[i] = re.sub('[,]', '', s[i])

#     for i in range(len(s)):
#         s[i] = list(map(int, s[i].split(',')))


#     for i in range(len(s)):
#         answer.append(int(s[i][0]))
#         for j in range(i+1, len(s)):
#             s[j] = re.sub(s[i][0], '', s[j])
    # print(answer)
    return answer

```
