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
    answer = s[0].upper()
    for i in range(1, len(s)):
        if answer[-1] == " ":
            if s[i] != " ":
                answer+= s[i].upper()
                continue
        answer+= s[i].lower()
            
    return answer

```

이틀에 걸쳐 푼 문제. 이유인 즉슨 문제를 잘못 이해하고 있었다..(바보)

중간에 공백이 많으면 "           "  이런 곳이 있으면 공백 하나로 치환해야 하는 줄 알았는데 공백은 그대로 놔둬야 하는 것이었다...

기존에 리스트로 변환 후 ' '.join() 을 통해 불필요한 공백 없애는 작업을 선행했는데 잘못 생각했다.

우선 answer 문자열에 첫번째 글자를 대문자로 넣는다. 

이후 반복문을 통해서 s를 하나씩 넣는데 answer의 마지막을 검사하며 넣을 것이기 때문에 미리 answer에 하나를 넣어둔 채로 시작한다.

만약 answer의 마지막이 공백인데, s도 공백이면 놔두는 것. s가 공백이 아니면 (앞이 공백이기에) 대문자로 넣고 continue

앞이 공백이 아니면 소문자 넣어주면 된다. 
