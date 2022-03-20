---
layout: post
title:  "프로그래머스 코딩테스트 문제4"
date:   2020-11-26 04:27 +0530
categories: python
---

알고리즘 풀기 25일차

오늘은 팀프로젝트로 개발하는 것이 있어,,,새벽까지 하다가 (사실 밤에 시작함) 이제서야 알고리즘 문제를 푼다. 

요즘 일찍 자는 연습을 하고있어 잠을 자고 싶기에,,,얼른 쉬운거 위주로 손을 대봤다. 

:)


- #서울에서 김서방 찾기

String형 배열 seoul의 element중 Kim의 위치 x를 찾아, 김서방은 x에 있다는 String을 반환하는 함수, solution을 완성하세요. seoul에 Kim은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.

```python

def solution(seoul):
    if 'Kim' in seoul:
        answer = "김서방은 {}에 있다".format(seoul.index('Kim'))
    return answer

```

---

- #문자열 내림차순으로 배치하기

문자열 s에 나타나는 문자를 큰것부터 작은 순으로 정렬해 새로운 문자열을 리턴하는 함수, solution을 완성해주세요.
s는 영문 대소문자로만 구성되어 있으며, 대문자는 소문자보다 작은 것으로 간주합니다.

```python

def solution(s):
    s = sorted(s, reverse = True)
    answer = ''.join(s)
    return answer

```

---

- #문자열 내 마음대로 정렬하기

문자열로 구성된 리스트 strings와, 정수 n이 주어졌을 때, 각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬하려 합니다. 
예를 들어 strings가 [sun, bed, car]이고 n이 1이면 각 단어의 인덱스 1의 문자 u, e, a로 strings를 정렬합니다.

```python 

def solution(strings, n):
    answer = []
    
    for i in range(len(strings)):
        strings[i] = strings[i][n]+strings[i]
        
    strings = sorted(strings)
    
    for i in range(len(strings)):
        answer.append(strings[i][1:])
    
    return answer

```

```python

def solution(strings, n):
    answer = []
    n_compare = []
    
    for i in range(0, len(strings)):
        n_compare.append(strings[i][n-1])
    
    n_compare = sorted(n_compare)
    
    if len(n_compare) == len(set(n_compare)):
        for i in range(0, len(n_compare)):
            for j in range(0, len(strings)):
                if n_compare[i][n-1] == strings[j][n-1]:
                    answer.append(strings[j])
    else:
        //생각하다 말았다.
    
    return answer
```

굉장히 복잡하게 생각하고 있어서 도저히 풀다가 코드가 길어질 것 같았다. 문자 하나하나 비교하기에 비효율적이고 그런 의도의 문제가 아닌거 같아 다른 사람들의 풀이를 봤는데 아니 굉장히 간단한 아이디어로 풀리는 것이었다.

충격. 

---

- #문자열 다루기 기본

문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요. 예를 들어 s가 a234이면 False를 리턴하고 1234라면 True를 리턴하면 됩니다.

```python

def solution(s):
    num = ['0','1','2','3','4','5','6','7','8','9']
    flag = []
    
    if len(s)<4 or len(s)>6 or len(s)==5:
        return False
    
    for i in range(len(s)):
        if s[i] in num:
            flag.append(1)
        else:
            flag.append(0)
    
    if sum(flag)==0 or sum(flag)==len(s):
        return True
    else:
        return False

```

문제에 비해 코드가 참 까탈스러운 거 같다. 테스트 자꾸 실패해서 보니 4또는 6의 길이만 갖는다 해서 다른 값 다 return false 해주니 잘 통과했다.

나는 숫자를 리스트로 미리 만들어놓고 숫자면 1을 넣고 문자면 0을 넣어서 숫자랑 문자랑 섞였는지 확인하도록 했다. 파이썬에서 isnan어쩌고가 있지만 사실 안써봐서 우선 이렇게 짜봤다. 

---

- #수박수박수박수박수박수?

길이가 n이고, 수박수박수박수....와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요. 예를들어 n이 4이면 수박수박을 리턴하고 3이라면 수박수를 리턴하면 됩니다.

```python

def solution(n):
    answer = ''
    watermelon="수박"
    if n%2==0:
        answer = watermelon*(n//2)
    else:
        answer = watermelon*(n//2)+"수"
    return answer

```

반복문을 쓸까 제일 먼저 떠올랐지만, 복잡도가 너무 커질 거 같아  - 비효율적이라 생각해서 짝수면 수박~, 홀수면 수박~에 수를 붙여서 출력해주는 방식으로 생각함.

---

이상 피곤해서 자야겠다,,,,




