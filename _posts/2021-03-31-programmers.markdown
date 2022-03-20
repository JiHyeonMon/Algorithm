---
layout: post
title:  "프로그래머스 코딩테스트"
date:   2021-03-31 23:59 +0530
categories: python
---

알고리즘 풀기 93일차

:)

- # 삼각 달팽이


# < 문제 >

정수 n이 매개변수로 주어집니다. 다음 그림과 같이 밑변의 길이와 높이가 n인 삼각형에서 맨 위 꼭짓점부터 반시계 방향으로 달팽이 채우기를 진행한 후, 첫 행부터 마지막 행까지 모두 순서대로 합친 새로운 배열을 return 하도록 solution 함수를 완성해주세요.

![image](https://user-images.githubusercontent.com/50662636/113160289-541f4b80-9278-11eb-9f79-beff47fc2468.png)

# < 제한사항 >

n은 1 이상 1,000 이하입니다.


# < 풀이 >

```python

import sys

# 함수에 들어갈 것
# n = 몇 칸 이동할지
# index 어디쪽 방향 & 빈 값에 넣을지 
def first(n, index, L_index):
     for i in range(n):
          for j in range(len(num[index])):
               if num[index][j] == 0:
                    num[index][j] = i
                    break

def second(n, index):
     for i in range(n):
          for j in range(len(num[index])):
               if num[index][j] == 0:
                    num[index][j] = i
                
def third(n, R_index):

n = int(sys.stdin.readline())

num = []
k = 0
L_index = 0
R_index = -1

# Initialize array  - set 0
for i in range(n):
     num.append([0 for j in range(i+1)])

# k is last number of array
k += for i in range(n, 0, -1)

while n > 0:
     # 1번 루트 - 배열 앞에 넣기
     # 2번 루트 - 맨 마지막 배열 순차로 (왼->오) 끝까지 채우기
     # 3번 루트 - 뒷 배열부터 맨 뒤에 넣기

print(num)

```

와,,,,점점 코드가 길어지는 중.

사실 아직 풀지 않음,,,그냥 규칙을 찾아는 냈으나 코딩을 하지 않은 상태,,,

오늘은 여기까지,,,ㅎㅎ (찡긋-) (내일의 내가 마무리 할 것이라 믿습니다.)