---
layout: post
title:  "프로그래머스 코딩테스트"
date:   2021-03-18 23:59 +0530
categories: python
---

알고리즘 풀기 88일차

:)

- # 전화번호 목록

# < 문제 >

전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

구조대 : 119

박준영 : 97 674 223

지영석 : 11 9552 4421

전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

# < 제한사항 >

phone_book의 길이는 1 이상 1,000,000 이하입니다.

각 전화번호의 길이는 1 이상 20 이하입니다.

같은 전화번호가 중복해서 들어있지 않습니다.

# < 풀이 >

```python

def solution(phone_book):
    answer = True
    phone_book = sorted(phone_book, key=len)
        
    for i in phone_book:
        tmp = ''
        for j in i:
            tmp += j
            if tmp in phone_book and tmp!=i:
                return False
    return True

```
정확성 테스트는 다 통과했는데, 효율성에서 두 개가 시간초과가 떴다.

테스트 1 〉	통과 (1.29ms, 11.1MB)
테스트 2 〉	통과 (1.32ms, 11MB)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	실패 (시간 초과)

참 시간초과 문제,,,,,,힘들다,,,,


---

```python

def solution(phone_book):
    answer = True
    phone_book = sorted(phone_book, key=len)
        
    for i in phone_book:
        tmp = ''
        for j in i:
            tmp += j
            if tmp in phone_book and tmp!=i:
                return False
    return True

```

---

또 두개 시간초과.

(된다는 풀이 찾아본건데도,,,,,,,,) 며칠전에 테스트케이스가 바꼈다고 한다.

아마 그래서 되던 풀이들이 안되나보다....

내일 다시 생각해보는 걸로,,,,