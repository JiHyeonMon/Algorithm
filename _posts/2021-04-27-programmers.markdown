---
layout: post
title: "[프로그래머스] SQL"
date: 2021-04-27 23:59 +0530
categories: 프로그래머스, SQL
---

알고리즘 풀기 108일차

오늘은 SQL 데이~
:)

# 최솟값 구하기

동물 보호소에 가장 먼저 들어온 동물은 언제 들어왔는지 조회하는 SQL 문을 작성해주세요.

## < 풀이 >

```sql

SELECT MIN(DATETIME) AS 시간 FROM ANIMAL_INS

```

where절 필요없이 min이용해서 시간이 제일 작은 것 출력

---

# 동물 수 구하기

동물 보호소에 동물이 몇 마리 들어왔는지 조회하는 SQL 문을 작성해주세요.

## < 풀이 >

```sql

SELECT COUNT(*) FROM ANIMAL_INS

```

행이 몇 개 있는지 count함수로 반환

---

# 중복 제거하기

동물 보호소에 들어온 동물의 이름은 몇 개인지 조회하는 SQL 문을 작성해주세요.

이때 이름이 NULL인 경우는 집계하지 않으며 중복되는 이름은 하나로 칩니다.

## < 풀이 >

```sql

SELECT COUNT(DISTINCT NAME) AS count
FROM ANIMAL_INS

```

중복 없앤 이름이 몇 개인지 반환

---

# 고양이와 개는 몇 마리 있을까

동물 보호소에 들어온 동물 중 고양이와 개가 각각 몇 마리인지 조회하는 SQL문을 작성해주세요.

이때 고양이를 개보다 먼저 조회해주세요.

## < 풀이 >

```sql

SELECT ANIMAL_TYPE, COUNT(*) as count
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE

```

동물 타입으로 그룹핑 --> 개와 고양이로 나뉜다.

여기서 고양이 cat이 더 먼저 나와야한다. dog 개가 알파벳 상으로 뒤라서 order by로 순서를 지정한다.

---

# NULL 처리하기

입양 게시판에 동물 정보를 게시하려 합니다. 동물의 생물 종, 이름, 성별 및 중성화 여부를 아이디 순으로 조회하는 SQL문을 작성해주세요. 이때 프로그래밍을 모르는 사람들은 NULL이라는 기호를 모르기 때문에, 이름이 없는 동물의 이름은 "No name"으로 표시해 주세요.

## < 풀이 >

```sql

SELECT ANIMAL_TYPE, IFNULL(NAME, 'No name'), SEX_UPON_INTAKE
FROM ANIMAL_INS
ORDER BY ANIMAL_ID

```

mysql의 isnull함수를 사용해서 NAME 값이 NULL이면 No name으로 설정

---

# 입양 시각 구하기(1)

보호소에서는 몇 시에 입양이 가장 활발하게 일어나는지 알아보려 합니다.

09:00부터 19:59까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문을 작성해주세요.

이때 결과는 시간대 순으로 정렬해야 합니다.

## < 풀이 >

```sql

SELECT HOUR(DATETIME) AS HOUR, COUNT(*) AS COUNT
FROM ANIMAL_OUTS
WHERE HOUR(DATETIME) BETWEEN '9' AND '19'
GROUP BY HOUR(DATETIME)
ORDER BY HOUR(DATETIME)

-- BETWEEN 아닌 > 8 만 했더니 틀림

```

테스트케이스에 끝이 19라서 끝은 생각안하고 부등호로 9부터 찍었는데 오류가 났다.

찾아보니 해당 시간 BETWEEN으로 설정해줘야 하는 문제!

    DATETIME 형식이 년, 월, 일, 시, 분, 초 이렇게 된 타입인데 우리는 분은 다 짜르고 시간만 볼 것이기에 HOUR함수를 통해 DATETIME에서 시간만 뽑아낼 수 있다.

---

# 루시와 엘라 찾기

동물 보호소에 들어온 동물 중 이름이 Lucy, Ella, Pickle, Rogan, Sabrina, Mitty인 동물의 아이디와 이름, 성별 및 중성화 여부를 조회하는 SQL 문을 작성해주세요.

## < 풀이 >

```sql

SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME='Ella' OR NAME = 'Lucy' OR NAME = 'Pickle' OR NAME='Rogan' OR NAME='Sabrina' OR NAME='Mitty'
ORDER BY ANIMAL_ID

```

이름 하나하나 비교해서 넣어줬다.

where절 통해서 해당 이름인 동물들 출력

---

# 이름에 el이 들어가는 동물 찾기

보호소에 돌아가신 할머니가 기르던 개를 찾는 사람이 찾아왔습니다. 이 사람이 말하길 할머니가 기르던 개는 이름에 'el'이 들어간다고 합니다.

동물 보호소에 들어온 동물 이름 중, 이름에 "EL"이 들어가는 개의 아이디와 이름을 조회하는 SQL문을 작성해주세요.

이때 결과는 이름 순으로 조회해주세요. 단, 이름의 대소문자는 구분하지 않습니다.

## < 풀이 >

```sql

SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE ANIMAL_TYPE = 'Dog' AND UPPER(NAME) LIKE '%EL%'
ORDER BY NAME

```

이름에 ~가 들어간, 정규표현식 및 그런 필터링을 찾아보았다.

생각한대로 % + ^ 이런 형식이 있었고 이럴 때는 칼럼 뒤에 LIKE를 써준다.

대소문자 구분하지 않기에 UPPER 함수를 통해 다 대문자로 올린뒤 EL로 확인.

---

# 중성화 여부 파악하기

보호소의 동물이 중성화되었는지 아닌지 파악하려 합니다.

중성화된 동물은 SEX_UPON_INTAKE 컬럼에 'Neutered' 또는 'Spayed'라는 단어가 들어있습니다.

동물의 아이디와 이름, 중성화 여부를 아이디 순으로 조회하는 SQL문을 작성해주세요.

이때 중성화가 되어있다면 'O', 아니라면 'X'라고 표시해주세요.

## < 풀이 >

```sql

SELECT ANIMAL_ID, NAME, IF(SEX_UPON_INTAKE LIKE 'Neutered%' OR SEX_UPON_INTAKE LIKE 'Spayed%', 'O', 'X') AS 중성화
FROM ANIMAL_INS
ORDER BY ANIMAL_ID

```

if문을 이용해서 SEX_UPON_INTAKE의 값이 Neutered로 시작하거나 Spayed로 시작하는지 확인해서 O, X로 값 세팅

---

# DATETIME에서 DATE로 형 변환

ANIMAL_INS 테이블에 등록된 모든 레코드에 대해, 각 동물의 아이디와 이름, 들어온 날짜1를 조회하는 SQL문을 작성해주세요. 이때 결과는 아이디 순으로 조회해야 합니다.

## < 풀이 >

```sql

SELECT ANIMAL_ID, NAME, DATE_FORMAT(DATETIME, '%Y-%m-%d') AS 날짜 FROM ANIMAL_INS ORDER BY ANIMAL_ID

```

날짜 형식 년, 월, 일, 시, 분, 초 인것을 DATE_FORMAT을 이용해서 원하는 형식으로 바꿀 수 있다.

---
