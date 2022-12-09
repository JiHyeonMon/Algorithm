---
layout: post
title:  "프로그래머스 코딩테스트 문제1"
date:   2020-11-22 23:52 +0530
categories: python
---

알고리즘 풀기 22일차

오랜만에 알고리즘 풀기~~~

프로그래머스의 쉬운 문제들을 풀어보는 시간을 가졌다!! *^^*

:)


- #두개 뽑아서 더하기

정수 배열 numbers가 주어집니다. numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.

```python
def solution(numbers):
    answer = []

    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            a = numbers[i]+numbers[j]
            if a not in answer:
                answer.append(a)
    answer = sorted(answer)
    return answer

```

---

- #완주하지 못한 선수

수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

```python

def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    for i in range(0, len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            break
            
    if answer == '':
        answer = participant[len(completion)]
    return answer

```

---

- #2016년

```python

2016년 1월 1일은 금요일입니다. 2016년 a월 b일은 무슨 요일일까요?

두 수 a ,b를 입력받아 2016년 a월 b일이 무슨 요일인지 리턴하는 함수, solution을 완성하세요. 요일의 이름은 일요일부터 토요일까지 각각 SUN,MON,TUE,WED,THU,FRI,SAT입니다. 예를 들어 a=5, b=24라면 5월 24일은 화요일이므로 문자열 TUE를 반환하세요.

def solution(a, b):
    sum = 0
    m = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    d = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    for i in range(a-1):
        sum += m[i]
    
    answer = d[(sum+b-1)%7]
    return answer

```

- #같은 숫자는 싫어

배열 arr가 주어집니다. 배열 arr의 각 원소는 숫자 0부터 9까지로 이루어져 있습니다. 이때, 배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거하려고 합니다. 단, 제거된 후 남은 수들을 반환할 때는 배열 arr의 원소들의 순서를 유지해야 합니다. 

예를 들면,

arr = [1, 1, 3, 3, 0, 1, 1] 이면 [1, 3, 0, 1] 을 return 합니다.

arr = [4, 4, 4, 3, 3] 이면 [4, 3] 을 return 합니다.

배열 arr에서 연속적으로 나타나는 숫자는 제거하고 남은 수들을 return 하는 solution 함수를 완성해 주세요.

```python

def solution(arr):
    answer = [arr[0]]
    for i in range(1,len(arr)):
        if arr[i-1]!=arr[i]:
            answer.append(arr[i])
    return answer

```

---

- #가운데 글자 가져오기

단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

```python

import math
def solution(s):
    answer = ''
    if len(s)%2==1:
        answer = s[math.floor(len(s)/2)]
    else:
        answer = s[len(s)//2-1]+s[len(s)//2]
    return answer

```

---

- #짝수와 홀수

정수 num이 짝수일 경우 Even을 반환하고 홀수인 경우 Odd를 반환하는 함수, solution을 완성해주세요.

```python

def solution(num):
    if num%2==0:
        answer = "Even"
    else:
        answer = "Odd"
    return answer

```

---

- #나누어 떨어지는 숫자 배열

array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.

divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.

```python

def solution(arr, divisor):
    answer = []
    for i in range(len(arr)):
        if arr[i]%divisor==0:
            answer.append(arr[i])
    
    if answer:
        answer = sorted(answer)
    else:
        answer.append(-1)
    return answer

```

- #두 정수 사이의 합

두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.

```python

def solution(a, b):
    answer = 0
    if b<a:
        a,b = b,a
        
    for i in range(a,b+1):
        answer += i
    return answer

```

- #문자열 내 p와 y의 개수

대문자와 소문자가 섞여있는 문자열 s가 주어집니다. s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요. 

'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.

예를 들어 s가 pPoooyY면 true를 return하고 Pyy라면 false를 return합니다.

```python

def solution(s):
    answer = True
    pc, yc = 0,0
    s = s.upper()
    for i in range(len(s)):
        if s[i] == 'P':
            pc+=1
        if s[i] == 'Y':
            yc+=1
    if pc==yc :
        answer = True
    else:
        answer = False
    return answer

```