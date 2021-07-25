---
layout: post
title: "[프로그래머스] JadenCase 문자열 만들기"
date: 2021-07-25 23:01
categories: 프로그래머스

---

알고리즘 풀기 234일차

:)

- # JadenCase 문자열 만들기


## < 문제 >

JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다. 

문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.

## < 풀이 >

```python

def solution(s):
    answer = []
    for i in range(0, len(s)):
        if s[i] == " ":
            answer.append(" ")
        else:
            answer.append(s[i].upper())
            p = i
            print(p)
            break
    # answer = s[0].upper()
    s = s[p:]
    print(s)
    s = ' '.join(s.lower().split())
    
    for i in range(p+1, len(s)):
        if answer[i-1] == ' ':
            answer += s[i].upper()
        else:
            answer += s[i]
    
    answer = ''.join(answer)
    return answer

```

