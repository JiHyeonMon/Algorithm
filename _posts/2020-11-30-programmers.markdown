---
layout: post
title:  "프로그래머스 코딩테스트 문제8"
date:   2020-11-30 00:45 +0530
categories: python
---

알고리즘 풀기 29일차

:)


- #내적

길이가 같은 두 1차원 정수 배열 a, b가 매개변수로 주어집니다. a와 b의 내적을 return 하도록 solution 함수를 완성해주세요.

이때, a와 b의 내적은 a[0]*b[0] + a[1]*b[1] + ... + a[n-1]*b[n-1] 입니다. (n은 a, b의 길이)

```python

def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer+=a[i]*b[i]
    return answer

```

내적이 뭔지 기억도 안난다. 들어가보니 굉장히 쉬운 문제.

---

- #[SQL]여러 기준으로 정렬하기

동물 보호소에 들어온 모든 동물의 아이디와 이름, 보호 시작일을 이름 순으로 조회하는 SQL문을 작성해주세요. 단, 이름이 같은 동물 중에서는 보호를 나중에 시작한 동물을 먼저 보여줘야 합니다.

```sql

SELECT ANIMAL_ID, NAME, DATETIME FROM ANIMAL_INS ORDER BY NAME, DATETIME DESC

```

이름 순 먼저, 이름 같다면 시간은 역순으로

---

- #[SQL]이름이 없는 동물의 아이디

동물 보호소에 들어온 동물 중, 이름이 없는 채로 들어온 동물의 ID를 조회하는 SQL 문을 작성해주세요. 단, ID는 오름차순 정렬되어야 합니다.

```SQL

SELECT ANIMAL_ID FROM ANIMAL_INS WHERE NAME IS NULL

```

---

- #k번째 수

배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.

예를 들어 array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면

array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.
1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.
2에서 나온 배열의 3번째 숫자는 5입니다.

배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands가 매개변수로 주어질 때, commands의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때 나온 결과를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

```python

def solution(array, commands):
    answer = []
    
    for i in range(0, len(commands)):
        start = commands[i][0]-1
        end = commands[i][1]
        num = commands[i][2]-1
        tmp = array[start:end]
        tmp = sorted(tmp)
        answer.append(tmp[num])
    return answer

```

변수를 안쓰고 할 수도 있었겠지만 이것저것 보기 불편할 거 같아서 변수로 세가지를 선언해줬다.
자를 배열의 시작 값 start, 배열의 끝 값 end, 자른 배열의 출력할 인덱스 num.

나머진 입력 commands의 개수에 따라 리스트를 1. 자르고 2. 정렬하고 3. 인덱스 값을 answer애 넣어주면 된다.

---

- #예산

S사에서는 각 부서에 필요한 물품을 지원해 주기 위해 부서별로 물품을 구매하는데 필요한 금액을 조사했습니다. 그러나, 전체 예산이 정해져 있기 때문에 모든 부서의 물품을 구매해 줄 수는 없습니다. 그래서 최대한 많은 부서의 물품을 구매해 줄 수 있도록 하려고 합니다.

물품을 구매해 줄 때는 각 부서가 신청한 금액만큼을 모두 지원해 줘야 합니다. 예를 들어 1,000원을 신청한 부서에는 정확히 1,000원을 지원해야 하며, 1,000원보다 적은 금액을 지원해 줄 수는 없습니다.

부서별로 신청한 금액이 들어있는 배열 d와 예산 budget이 매개변수로 주어질 때, 최대 몇 개의 부서에 물품을 지원할 수 있는지 return 하도록 solution 함수를 완성해주세요.

```python

def solution(d, budget):
    answer = 0
    d = list(sorted(d))
    s,cnt = 0,0
    if sum(d)<=budget:
        return len(d)
    else:
        for i in range(len(d)):
            s+=d[i]

            if s<=budget:
                cnt+=1
            else:
                break

    return cnt

```

예산에 맞는지 d를 정렬해서 작은 애부터 더해가다 예산을 넘으면 카운트를 그만하는 방식으로 코드를 짰다.

---

이 다음으로 프로그래머스 1단계 문제로 카카오2019 문제 '실패율' 하나 남았는데 이건 저번에 풀었다가 시간초과가 몇 케이스 떠서 89점,,,11점이 모자란 상황,,,
내일 이거 수정해서 프로그래머스 1단계 다 해치워 버릴 것.

백준을 풀까도 싶었는데 뭔가 프로그래머스 문제 수가 많지 않은데 다 완전 섞인 느낌이라 짧게 훑기 좋은 것 같다. 짧지 않았을 수 있지만. 

한 2-3단계까지 더 풀어보고 백준으로 돌아갈까 싶기도 하다. (사실 2단계부턴 너무 어려워질 것 같기도 하다. )