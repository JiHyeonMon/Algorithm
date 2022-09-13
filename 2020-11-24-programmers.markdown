---
layout: post
title:  "프로그래머스 코딩테스트 문제3"
date:   2020-11-25 01:59 +0530
categories: python
---

알고리즘 풀기 24일차

오늘은 놀다 들어와서 늦게 올린다ㅠㅠㅠㅠ

:)


- #직사각형 별 찍기

이 문제에는 표준 입력으로 두 개의 정수 n과 m이 주어집니다.
별(*) 문자를 이용해 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 출력해보세요.

```python
a, b = map(int, input().strip().split(' '))
for i in range(b):
    print('*'*a)

```

Very easy- thank you very much-

---

- #핸드폰 번호 가리기

자연수 n이 매개변수로 주어집니다. n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.

```python

def solution(phone_number):
    answer = '*'*(len(phone_number)-4)+phone_number[len(phone_number)-4:]
    return answer

```

아래와 같이 처음에 짰는데, 기본 테스트 케이스 두개는 통과했는데 나머진 다 실패.

도대체 왜???? 그래서 결국 다시 위의 코드로 짜니까 바로 맞췄다. (긁적)

```python

def solution(phone_number):
    for i in range(len(phone_number)-4):
        phone_number = phone_number.replace(phone_number[i], '*')
    return phone_number

```

---

- #이름이 있는 동물의 아이디

동물 보호소에 들어온 동물 중, 이름이 있는 동물의 ID를 조회하는 SQL 문을 작성해주세요. 단, ID는 오름차순 정렬되어야 합니다.

```sql

SELECT ANIMAL_ID FROM ANIMAL_INS WHERE NAME IS NOT NULL

```

---

- #상위 n개 레코드

동물 보호소에 가장 먼저 들어온 동물의 이름을 조회하는 SQL 문을 작성해주세요.

```sql

SELECT NAME FROM ANIMAL_INS ORDER BY DATETIME LIMIT 1

```

limit은 나도 처음 써봤다.

order로 정렬해준후 최상위 1개만 출력하고 싶어 limit을 썼다.

---

- #x만큼 간격이 있는 n개의 숫자

함수 solution은 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다. 다음 제한 조건을 보고, 조건을 만족하는 함수, solution을 완성해주세요.

```python

def solution(x, n):
    answer = []
    plus = x
    while len(answer)<n:
        answer.append(x)
        x += plus
    return answer

```

---

- #하샤드 수

양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다. 예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다. 자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, solution을 완성해주세요.

```python

def solution(x):
    sum = 0
    for i in range(len(str(x))):
        sum += int(str(x)[i])
        
    if x%sum == 0:
        return True
    else:
         return False

```

---

- #행렬의 덧셈

행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다. 2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.

```python

def solution(arr1, arr2):
    answer = [[0 for i in range(len(arr1[0]))] for i in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            answer[i][j]= arr1[i][j]+arr2[i][j]
    return answer

```


