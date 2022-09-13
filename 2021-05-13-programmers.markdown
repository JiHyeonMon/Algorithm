---
layout: post
title: "[프로그래머스] 전화번호 목록"
date: 2021-05-13 23:33 +0530
categories: 프로그래머스 해시
---

알고리즘 풀기 117일차

:)

- # 전화번호 목록

>

## < 문제 >

전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.

전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

    구조대 : 119
    박준영 : 97 674 223
    지영석 : 11 9552 4421

전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

## < 입력형식 >

phone_book의 길이는 1 이상 1,000,000 이하입니다.

각 전화번호의 길이는 1 이상 20 이하입니다.

같은 전화번호가 중복해서 들어있지 않습니다.

## < 풀이 >

```python
# 정확성 100, 효율성 2/4
def solution(phone_book):
    answer = True
    num = len(phone_book)
    phone_book = sorted(phone_book, key=len)

    for i in range(num):
        for j in range(i+1, num):
            if phone_book[i] == phone_book[j][:len(phone_book[i])]:
                return False
    return True

```

우선 길이 순으로 정렬을 한다.

짧은 게 당연히 더 긴 번호의 접두어가 될 수 있으니 반복문을 통해 해당 전화번호가 그 뒤 전화번호들과 같은지 비교하고 같으면 return False로 끝.

근데 효율성에서 두개가 안맞는데,,,

잠이 오는 관계로 내일,,,마저,,,,
