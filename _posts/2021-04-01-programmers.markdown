---
layout: post
title: "프로그래머스 코딩테스트"
date: 2021-04-01 23:59 +0530
categories: python
---

알고리즘 풀기 94일차

회사에서 몰래 풀었는데, 몰래몰래 조금씩 풀다보니 주석을 자꾸 달게된다. (순간순간 생각한 알고리즘 까먹을까봐)

:)

- # 삼각 달팽이

## < 문제 >

정수 n이 매개변수로 주어집니다. 다음 그림과 같이 밑변의 길이와 높이가 n인 삼각형에서 맨 위 꼭짓점부터 반시계 방향으로 달팽이 채우기를 진행한 후, 첫 행부터 마지막 행까지 모두 순서대로 합친 새로운 배열을 return 하도록 solution 함수를 완성해주세요.

![image](https://user-images.githubusercontent.com/50662636/113160289-541f4b80-9278-11eb-9f79-beff47fc2468.png)

## < 제한사항 >

n은 1 이상 1,000 이하입니다.

## < 풀이 >

```python

iimport sys

#함수에 들어갈 것
# n = 몇 칸 이동할지
# index 어디쪽 방향 & 빈 값에 넣을지
def first(n, array_index, index, a):
    for i in range(n):
        num[array_index][index] = a
        array_index += 1
        a += 1
    n -= 1
    index += 1 # 왼쪽 칸 다 채움
    array_index -= 1 # 마지막까지 간 후 +1 하고 나옴
    return n, array_index, index, a

def second(n, array_index, index, a):
    for i in range(n):
        num[array_index][index] = a
        index+=1
        a+=1
    n -= 1
    index -= 2 # 마지막 배열 다 채움, 왼쪽 맨 마지막 인덱스 값
    array_index -= 1 # 마지막 다 채웠으니 왼쪽으로 한 칸 이동 ( 이 다음은 왼쪽으로 갈 것 )
    return n, array_index, index, a

def third(n, array_index, index, a):
    for i in range(n):
        num[array_index][index] = a
        a += 1
        index-=1 # 앞 칸 갈 수록 맨 끝 index 도 줄어든다.
        array_index -= 1
    n -= 1
    array_index += 1 # 이제 다시 오른 쪽으로 갈 것. 다음 차례 오른쪽 배열로 세팅
    return n, array_index, index, a

n = int(sys.stdin.readline())

num = []
array_index = 0
index = 0
a = 1

# Initialize array  - set 0
for i in range(n):
    num.append([0 for j in range(i+1)])

while n > 0:
    # 1번 루트 - 배열 앞에 넣기
    n, array_index, index, a = first(n, array_index, index, a)
    # 2번 루트 - 맨 마지막 배열 순차로 (왼->오) 끝까지 채우기
    n, array_index, index, a = second(n, array_index, index, a)
    # 3번 루트 - 뒷 배열부터 맨 뒤에 넣기
    n, array_index, index, a = third(n, array_index, index, a)

    array_index += 1
    index += 1

print(sum(num, []))

```

삼각 달팽이, 그림으로 보면 삼각 달팽이지만 (ㅋㅋㅋ) 사실 입출력 값을 보면 그냥 배열을 써야겠다 생각이 들었고 규칙 찾기에 먼저 전념했다.

우선 총 세 개의 액션으로 나눌 수 있다. 아래 세 스텝의 반복으로 이뤄진다.

> 첫째, 왼쪽 대각선 내려가는 부분.

> 둘째, 맨 밑의 줄 가로로 순차적 채우기

> 셋째, 오른쪽 대각선 올라가는 부분

(예로 입력을 6이라 가정)

6이 들어오면 우선 0으로 채워진 배열을 먼저 만들었다. ==> [[0], [0,0], [0,0,0], [0,0,0,0], [0,0,0,0,0], [0,0,0,0,0,0]]

> 첫번째 스텝, [[1], [2,0], [3,0,0], [4,0,0,0], [5,0,0,0,0], [6,0,0,0,0,0]] ==> 6번 진행

> 두번째 스텝, [[1], [2,0], [3,0,0], [4,0,0,0], [5,0,0,0,0], [6,7,8,9,10,11]] ==> 5번 진행

> 세번째 스텝, [[1], [2,15], [3,0,14], [4,0,0,13], [5,0,0,0,12], [6,7,8,9,10,11]] ==> 4번 진행

> 첫번째 스텝, [[1], [2,15], [3,16,14], [4,17,0,13], [5,18,0,0,12], [6,7,8,9,10,11]] ==> 3번 진행

> 두번째 스텝, [[1], [2,15], [3,16,14], [4,17,0,13], [5,18,19,20,12], [6,7,8,9,10,11]] ==> 2번 진행

> 세번째 스텝, [[1], [2,15], [3,16,14], [4,17,21,13], [5,18,19,20,12], [6,7,8,9,10,11]] ==> 1번 진행

입력 값 n 만큼 스텝을 돈다는 것을 발견

그리하여 실제 코드를 보면 n만큼 while문을 돌며 각 스텝을 순차적으로 호출하며 n을 감소시킨다.

그리고 array_index는 n만큼 진행할테니 끝나는 부분은 몰라도 되는데 어느 배열에서 시작하는지 위치가 필요하고, 그 배열 안에서 몇 번째에 값을 넣어줘야하는지 index도 필요하여 두개의 변수로 위치를 찾아간다.

> 첫째, 왼쪽 대각선 내려가는 부분. ==> array_index 증가 (아래=뒤로 이동), index는 고정 (맨 처음일 경우 [0]이 되고 그렇기에 맨 앞에 값들 채워짐)

> 둘째, 맨 밑의 줄 가로로 순차적 채우기 ==> array_index 고정 (맨 뒤에 칸 채우기), index 증가

> 셋째, 오른쪽 대각선 올라가는 부분 ==> array_index 감소 (위=앞으로 이동), index 줄어듬(앞 배열일수록 개수가 작아서 하나씩 줄여줌)

위와 같은 규칙으로 코드를 짰다.
