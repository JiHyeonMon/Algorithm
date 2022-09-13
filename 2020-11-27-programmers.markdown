---
layout: post
title:  "프로그래머스 코딩테스트 문제5"
date:   2020-11-27 04:00 +0530
categories: python
---

알고리즘 풀기 26일차

:)


- #소수 찾기

1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.

소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
(1은 소수가 아닙니다.)

```python

import math
def solution(n):
    answer = 0

    for i in range(2,n+1):
        isP = True
        for j in range(2, int(math.sqrt(i))+1):
            if i%j==0:
                isP=False
                break
        if isP == True:
            answer+=1
            
    return answer

```

---

- #문자열을 정수로 바꾸기

문자열 s를 숫자로 변환한 결과를 반환하는 함수, solution을 완성하세요.

```python

def solution(s):
    answer = 0
    if s[0]=='-':
        answer = -1*int(s[1:])
    elif s[0]=='+':
        answer = int(s[1:])
    else:
        answer = int(s)
    return answer

```

---

- #시저암호

어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다. 예를 들어 AB는 1만큼 밀면 BC가 되고, 3만큼 밀면 DE가 됩니다. z는 1만큼 밀면 a가 됩니다. 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.

```python 

def solution(s, n):
    answer = ''
    for i in range(0,len(s)):
        if s[i]==" ":
            answer+=" "
        elif s[i].isupper():
                answer+=chr((ord(s[i])-ord('A')+n)%26+ord('A'))
        else:
            answer+=chr((ord(s[i])-ord('a')+n)%26+ord('a'))
    return answer

```

아스키코드 숫자를 이용해서 풀었다. 

ord = 문자를 아스키숫자로
chr = 아스키숫자를 문자로

---

- #평균 구하기

정수를 담고 있는 배열 arr의 평균값을 return하는 함수, solution을 완성해보세요.

```python

def solution(arr):
    return sum(arr)/len(arr)

```

또잉스러운 문제

---

- #약수의 합

정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.

```python

def solution(n):
    answer = []
    for i in range(1, n+1):
        if n%i==0:
            answer.append(i)
    return sum(answer)

```

---

- #자릿수 더하기

자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.

```python
def solution(n):
    answer = 0
    s = str(n)
    for i in range(0, len(s)):
        answer+=int(s[i])
    return answer

```

---

- #자연수 뒤집어 배열로 만들기

자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

```python

def solution(n):
    answer = list(map(int, list(str(n))))
    return list(reversed(answer))

```

---

- #제일 작은 수 제거하기

정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수, solution을 완성해주세요. 단, 리턴하려는 배열이 빈 배열인 경우엔 배열에 -1을 채워 리턴하세요. 예를들어 arr이 [4,3,2,1]인 경우는 [4,3,2]를 리턴 하고, [10]면 [-1]을 리턴 합니다.

```python

def solution(arr):
    if len(arr)==1:
        return [-1]
    
    m = min(arr)
    arr.pop(arr.index(m))
    
    return arr

```

---

- #콜라츠 추측

1937년 Collatz란 사람에 의해 제기된 이 추측은, 주어진 수가 1이 될때까지 다음 작업을 반복하면, 모든 수를 1로 만들 수 있다는 추측입니다. 작업은 다음과 같습니다.

1-1. 입력된 수가 짝수라면 2로 나눕니다. 
1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다.
2. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복합니다.

예를 들어, 입력된 수가 6이라면 6→3→10→5→16→8→4→2→1 이 되어 총 8번 만에 1이 됩니다. 위 작업을 몇 번이나 반복해야하는지 반환하는 함수, solution을 완성해 주세요. 단, 작업을 500번을 반복해도 1이 되지 않는다면 –1을 반환해 주세요.

```python

def solution(num):
    cnt = 0
    while num!=1:
        if cnt==500:
            return -1
        if num%2==0:
            num /=2
        else:
            num=num*3+1
        cnt+=1
        
    return cnt

```

---

- #최대공약수와 최소공배수

두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요. 배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다. 예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.

```python

def solution(n, m):
    answer = []
    a = []
    b = []
    for i in range(1, max(n,m)+1):
        if n%i==0 and m%i==0:
            answer.append(i)
        
    return [max(answer), n*m//max(answer)]

```

최대공약수는 쉽게 생각해냈는데 최소공배수 넘나리 오랜만이라 그냥 둘 곱해버렸는데

최소공배수 = 두수의 곱 / 최대공약수    *^^* 기억하자

---

- #정수제곱근 판별

임의의 양의 정수 n에 대해, n이 어떤 양의 정수 x의 제곱인지 아닌지 판단하려 합니다.
n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.

```python

import math
def solution(n):
    if math.sqrt(n) == int(math.sqrt(n)):
        return int(math.sqrt(n)+1)**2
    else:
        return -1

```

분명 sqrt제대로 되는지 왜 안되지 했는데 sqrt처리가 제대로 돼도 11.0 이렇게 float타입으로 나워서 나눠떨어지는 숫자인지 int()형변환한 값과 비교해서 제곱수인지 판단.

---

- #정수 내림차순으로 배치하기

함수 solution은 정수 n을 매개변수로 입력받습니다. n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 예를들어 n이 118372면 873211을 리턴하면 됩니다.

```python

def solution(n):
    answer = sorted(list(str(n)), reverse = True)
    return int(''.join(answer))

```

---

- #이상한 문자 만들기

문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 각 단어는 하나 이상의 공백문자로 구분되어 있습니다. 각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.

제한 사항
문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야합니다.
첫 번째 글자는 0번째 인덱스로 보아 짝수번째 알파벳으로 처리해야 합니다.

```python

def solution(s):
    answer = ''
    word = list(s.split(' '))
    for i in range(0,len(word)):
        for j in range(0,len(word[i])):
            if j%2==0:
                answer+=word[i][j].upper()
            else:
                answer+=word[i][j].lower()
        answer+=" "
        
    return answer[:len(answer)-1]

```

아니 31점 나왔는데 아무리 봐도 문제 없는데 뭘까 찾아보니 split(' ')으로 해줘야한다는 것. 원래 .spilt()으로 썼음.
이런 사소한 문제 찾기가 참 힘들다ㅠ.

---

오늘 이렇게 많이 푼 이유는, 약간 강박? 같은 것도 있지만 프로그래머스로 풀면서 단게별로 1단계부터 시작하는데 이제 1단계의 연.습.문.제.를 다 풀었다!!!!!! 다 풀려고 두시간 가까이,,쓴 거 같다. 게중에 1단계 카카오나 다른 실제 기출 푼 것도 있지만, 내일은 1단게의 정렬이나 탐색, 탐욕법 같은 문제를 하나하나 풀어갈 것이고 곧 2단계 문제를 풀 것이다.

그래도 당분간 쉬운거 풀면서 재밌었다 *^^*