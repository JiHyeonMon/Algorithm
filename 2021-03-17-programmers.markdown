---
layout: post
title:  "프로그래머스 코딩테스트"
date:   2021-03-17 23:59 +0530
categories: python
---

알고리즘 풀기 87일차

:)

- #큰 수 만들기

# < 문제 >

어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.

예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다. 이 중 가장 큰 숫자는 94 입니다.

문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다. number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return 하도록 solution 함수를 완성하세요.

# < 제한사항 >

number는 1자리 이상, 1,000,000자리 이하인 숫자입니다.

k는 1 이상 number의 자릿수 미만인 자연수입니다.

# < 풀이 >

```python

def solution(number, k):
    stack = []
    for i in range(len(number)):
        if not stack:
            stack.append(number[i])
            continue
        
        isRemove = False
        while stack and int(stack[-1]) < int(number[i]):
            stack.pop()
            k -= 1
            if not k:
                isRemove = True
                stack += number[i:]
                break
        
        if isRemove:
            break
        
        stack.append(number[i])
        
    return "".join(stack[:len(number) - k]) if k else "".join(stack)

```

입력받은 number만큼 우선 반복문을 돌린다.

정답을 넣은 stack이라는 배열을 만든다. 여기에 stack이 비면 해당 인덱스의 값을 넣고 시작한다.

stack에 값이 있으면서 맨 마지막 stack의 값이 해당 인덱스의 값보다 작다면 stack에서 뺀다. (한 자리 뺐으니 k 감소)

k 가 false 즉 0이면, 뺄 자리 수 다 뺐다는 것 == 뒤의 나머지 값 다 넣고 반복문을 멈춰주면 된다.

---

ㅎㅎㅎ 어우 빡친다;; 결국은 풀이를 찾아봤다.

진짜 풀이 생각해 낸 것과 비슷한데, 왜 코드로 못짤까. 이건 나의 머리와 생각을 하다 마는 내 의지의 문제 같다.

진짜 날이 갈 수록 멍청이가 되어가는 것 같다. 내가 열심히 안풀어서가 제일 큰 문제.

풀어서 찝찝함은 가셨지만, 진짜,,,공부의 필요성을 느낀 하루다.