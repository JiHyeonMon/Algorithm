---
layout: post
title:  "프로그래머스 코딩테스트"
date:   2021-03-16 23:59 +0530
categories: python
---

알고리즘 풀기 86일차

:)

- #큰 수 만들기

# <문제 설명>

어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.

예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다. 이 중 가장 큰 숫자는 94 입니다.

문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다. number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return 하도록 solution 함수를 완성하세요.

# <제한사항>

number는 1자리 이상, 1,000,000자리 이하인 숫자입니다.

k는 1 이상 number의 자릿수 미만인 자연수입니다.

# <풀이>

```python

def solution(number, k):
    answer = ''
    while k>0:
        for i in range(len(number)-k):
            if number[i]<number[i+1]:
                number = number.replace(number[i], '', 1)
                k-=1
                break
            else:
                pass

        
    return number

```

3/12 시간초과

# <풀이>

```python

def solution(number, k):
    answer = ''
    while k>0:
        for i in range(len(number)):
            if number[i]<number[i+1]:
                number = number.replace(number[i], '', 1)
                k-=1
                break
            else:
                pass

        
    return number

```

# <풀이>

1/12 시간초과, 1/12 런타임 에러

```python

def solution(number, k):
    answer = ''
    lst = list(number)
    i = 0
    while k > 0:
        if number[i] < number[i+1]:
            number = number.replace(number[i], '', 1)
            k -= 1
            i = 0
        else:
            i += 1
            pass
        
    return number

```

2/12 시간초과, 1/12 런타임에러

반복문을 하나로 줄였는데도 시간초과가 뜬다. 

===

오늘 더 수정해보려했는데 이만 자야할 것 같다ㅠㅠ내일 진짜 다 통과 만들고 만다,,,,