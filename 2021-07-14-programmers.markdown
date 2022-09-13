---
layout: post
title: "[프로그래머스] 문자열 압축"
date: 2021-07-14 23:01
categories: 프로그래머스 2020카카오
---

알고리즘 풀기 230일차

:)

- # 문자열 압축

## < 문제 >

데이터 처리 전문가가 되고 싶은 "어피치"는 문자열을 압축하는 방법에 대해 공부를 하고 있습니다.

최근에 대량의 데이터 처리를 위한 간단한 비손실 압축 방법에 대해 공부를 하고 있는데, 문자열에서 같은 값이 연속해서 나타나는 것을 그 문자의 개수와 반복되는 값으로 표현하여 더 짧은 문자열로 줄여서 표현하는 알고리즘을 공부하고 있습니다.

간단한 예로 "aabbaccc"의 경우 "2a2ba3c"(문자가 반복되지 않아 한번만 나타난 경우 1은 생략함)와 같이 표현할 수 있는데, 이러한 방식은 반복되는 문자가 적은 경우 압축률이 낮다는 단점이 있습니다.

예를 들면, "abcabcdede"와 같은 문자열은 전혀 압축되지 않습니다.

"어피치"는 이러한 단점을 해결하기 위해 문자열을 1개 이상의 단위로 잘라서 압축하여 더 짧은 문자열로 표현할 수 있는지 방법을 찾아보려고 합니다.

예를 들어, "ababcdcdababcdcd"의 경우 문자를 1개 단위로 자르면 전혀 압축되지 않지만, 2개 단위로 잘라서 압축한다면 "2ab2cd2ab2cd"로 표현할 수 있습니다.

다른 방법으로 8개 단위로 잘라서 압축한다면 "2ababcdcd"로 표현할 수 있으며, 이때가 가장 짧게 압축하여 표현할 수 있는 방법입니다.

다른 예로, "abcabcdede"와 같은 경우, 문자를 2개 단위로 잘라서 압축하면 "abcabc2de"가 되지만, 3개 단위로 자른다면 "2abcdede"가 되어 3개 단위가 가장 짧은 압축 방법이 됩니다.

이때 3개 단위로 자르고 마지막에 남는 문자열은 그대로 붙여주면 됩니다.

압축할 문자열 s가 매개변수로 주어질 때, 위에 설명한 방법으로 1개 이상 단위로 문자열을 잘라 압축하여 표현한 문자열 중 가장 짧은 것의 길이를 return 하도록 solution 함수를 완성해주세요.

## < 풀이 >

```python

from collections import deque
def solution(s):
    answer = []

    # 테케 s:"a"
    if len(s) == 1:
        return 1

    for i in range(1, len(s)//2+1) :
        step = [s[0:i]]
        cnt = 1
        for j in range(i, len(s), i):
            tmp = s[j:j+i]
            if step[-1] == tmp:
                cnt += 1
            else :
                if cnt != 1:
                    step.append(str(cnt))
                step.append(tmp)
                cnt = 1

        if cnt != 1:
            step.append(str(cnt))

        answer.append(len(''.join(step)))
    return min(answer)

```

이전에 풀다 만 문제 다시 풀었다.

진짜 조건문과 반복문의 향연,,,

우선 문자를 자르는데 1개씩 자르는 것부터 최대 input s의 절반 크기로 자른다. (절반 크기로 자르면 반이 돼서 2개로 나뉘기에 그 이상의 크기로 잘라도 2개)

각각 자른 것을 step에 넣고 다음 것을 비교하는데 현재 칸을 tmp에 넣고 step에 담긴 마지막 칸을 보고 비교한다.

tmp(현재)가 step[-1] (한칸 전)과 같다면 tmp는 넣을 필요 없고, 같은 개수를 세어주는 cnt를 증가시킨다.

만약 다를 경우, 1인 경우 들어가지 않기에 빼고 cnt를 넣어준다. (이전 step[-1]와 같은게 몇 개 나왔는지)

그리고 현재 step의 마지막과 달랐던 현재 tmp를 넣어준다. (반복)

제일 마지막은 cnt가 안들어가기에 for문을 나와서 검사해서 cnt를 넣어준다.

"ababcdcdefcd" 가령 이런 예가 있다면 4개로 끊었을 때, ["abab", "2", "cdcd", "2", "efcd"] 이렇게 들어가게 되는 셈이다.

그래서 해당 배열을 하나의 string으로 join하여 "abab2cdcd2efcd"이렇게 만들고 이것의 길이를 answer에 넣는다.

<문제의 예에선 2abab2cdcdefcd 이렇게지만 난 편의를 위해 count를 해당 반복문자 뒤에 넣었다.>

그리고 가장 짧은 길이를 반환해준다.

아래는 기존 틀린 코드.

```python

from collections import deque
def solution(s):
    answer = 0

    for i in range(2, len(s)//2+1):
        tmp = [ s[j:j+i] for j in range(0, len(s), i) ]
        tmp = deque(tmp)
        compress = deque(tmp.popleft())

        while tmp:
            cnt = 0
            compress.append(tmp.popleft())
            if compress[-1] == compress[-2]:
                compress.pop()
                cnt += 1
            else:
                if cnt:
                    compresss.append(cnt)
                    cnt = 0
        print(compress)
    return answer

```
