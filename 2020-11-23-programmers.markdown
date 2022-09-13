---
layout: post
title:  "프로그래머스 코딩테스트 문제2"
date:   2020-11-23 23:59 +0530
categories: python
---

알고리즘 풀기 23일차

더 풀고 싶었는데,,,좀 늦게 시작한 감이 없잖아있네요.,,호호

:)


- #최대값 구하기

ANIMAL_INS 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블입니다. ANIMAL_INS 테이블 구조는 다음과 같으며, ANIMAL_ID, ANIMAL_TYPE, DATETIME, INTAKE_CONDITION, NAME, SEX_UPON_INTAKE는 각각 동물의 아이디, 생물 종, 보호 시작일, 보호 시작 시 상태, 이름, 성별 및 중성화 여부를 나타냅니다.

가장 최근에 들어온 동물은 언제 들어왔는지 조회하는 SQL 문을 작성해주세요.


```sql
SELECT MAX(DATETIME) AS '시간' FROM ANIMAL_INS

```

---

- #3진법 뒤집기

자연수 n이 매개변수로 주어집니다. n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.


```python

def solution(m):
    multi = []
    answer = []
    i=0
    sum = 0
    while m>=3:
        if 3**i>m:
            multi.append(i-1)
            m -= 3**(i-1)
            i=0
        else:
            i+=1
    for i in range(m):multi.append(0)

    for i in range(max(multi), -1, -1):
        if i in multi:
             answer.append(multi.count(i))
        else:
             answer.append(0)
    
    answer = list(reversed(answer))

    for i in range(0, len(answer)):
        sum+=answer[len(answer)-i-1]*(3**i)

    return sum

```

상당히,,,진법 계산이 귀찮고 귀찮은 문제였다.

입력으로 주어진 10진수 n을 3진수로 바꾸고 해당 3진수를 거꾸로 쓴 수를 10진수로 바꾸는 문제다.

진법 변환이 파이썬에서 제공할 줄 알았는데 흔히들 쓰는 진법만 제공하고 3진법은 못찾은? 모르겠다. 그냥 만들어봤다.

입력 값과 3의 진수를 비교하여 입력 값보다 작지만 근사한 3의 진수를 구해 지수를 리스트에 넣고 입력 값에서 해당 수를 뺀 후 반복한다.

그렇게 3의 진수씩 빼가며 3보다 작게 남았을 때는 1,2 이런 경우는 0을 그만큼 곱해서 넣어줘서 지수승에 해당하는게 몇번에 걸쳐 있는지 리스트에 넣는다.

예를 들면, 125 는 [4,3,2,1,1,0,0] --> 해당 리스트를 다시 반복 돌려 반복되는 수 카운트 해서 처리해주면 11122 이렇게 3진법으로 바꿀 수 있다.

이것을 reversed()를 이용해 아예 22111로 바꿔준다.

마찬가지로 반복문 돌며 3의 지수승 곱해주며 10진법으로 다시 변환한다.

---