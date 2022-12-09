---
layout: post
title: "[프로그래머스] N개의 최소공배수"
date: 2021-07-05 23:01 +0530
categories: 프로그래머스 최소공배수 최대공약수
---

알고리즘 풀기 228일차

정말 오랜만입니다. 사실 아직 통과도 아닌,,,,,풀다 만 문제,,,,,,

오랜만에 펴봤으니 만족- 하하하,,,,,,,,,,

오랜만에 왔더니 머리가 안돌아가고,,얼른 눕고싶고,,,,,암턴,,,,그렇네여,,,,,ㅠㅠㅠㅠㅠㅠ

:)

- # N개의 최소공배수
  >

## < 문제 >

두 수의 최소공배수(Least Common Multiple)란 입력된 두 수의 배수 중 공통이 되는 가장 작은 숫자를 의미합니다. 예를 들어 2와 7의 최소공배수는 14가 됩니다.

정의를 확장해서, n개의 수의 최소공배수는 n 개의 수들의 배수 중 공통이 되는 가장 작은 숫자가 됩니다.

n개의 숫자를 담은 배열 arr이 입력되었을 때 이 수들의 최소공배수를 반환하는 함수, solution을 완성해 주세요.

## < 풀이 >

```python

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def lcm(a, b):
    return a*b//gcd(a, b)

def solution(arr):
    answer = 0
    arr = sorted(arr)
    answer = lcm(arr.pop(), arr.pop())

    while arr:
        num = arr.pop()
        if num == 1:
            return answer

        if lcm(answer, num) == answer:
            return answer
        else:
            answer = lcm(answer, num)

```

생각한 로직은 크기 순으로 숫자를 정렬한 후, 가장 큰 두 수의 최소 공배수를 구한다.

그러고 그 다음 수와 비교했을 때 최소 공배수가 다를 경우, 그 수와 이전에 구한 최소 공배수의 최소공배수를 구해나가는 방식.

근데 틀렸다. 다시 접근해야할 거 같다.
