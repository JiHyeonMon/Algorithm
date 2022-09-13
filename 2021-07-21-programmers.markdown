---
layout: post
title: "[프로그래머스] 거리두기 확인하기"
date: 2021-07-21 23:01
categories: 프로그래머스 2021카카오

---

알고리즘 풀기 233일차

:)

- # 거리두기 확인하기


## < 문제 >

개발자를 희망하는 죠르디가 카카오에 면접을 보러 왔습니다.

코로나 바이러스 감염 예방을 위해 응시자들은 거리를 둬서 대기를 해야하는데 개발 직군 면접인 만큼 아래와 같은 규칙으로 대기실에 거리를 두고 앉도록 안내하고 있습니다.

  > 대기실은 5개이며, 각 대기실은 5x5 크기입니다.

  > 거리두기를 위하여 응시자들 끼리는 맨해튼 거리1가 2 이하로 앉지 말아 주세요.

  > 단 응시자가 앉아있는 자리 사이가 파티션으로 막혀 있을 경우에는 허용합니다.

예를 들어,

![image](https://user-images.githubusercontent.com/50662636/126506604-b0cab0af-2171-4eaa-88ec-68c54c06e694.png)

5개의 대기실을 본 죠르디는 각 대기실에서 응시자들이 거리두기를 잘 기키고 있는지 알고 싶어졌습니다. 

자리에 앉아있는 응시자들의 정보와 대기실 구조를 대기실별로 담은 2차원 문자열 배열 places가 매개변수로 주어집니다. 

각 대기실별로 거리두기를 지키고 있으면 1을, 한 명이라도 지키지 않고 있으면 0을 배열에 담아 return 하도록 solution 함수를 완성해 주세요.

## < 풀이 >

```python

def check(i, j, place):
    # 상
    if i>0 and place[i-1][j] == 'P' :
        return False
    if i>1 and place[i-2][j] == 'P' and place[i-1][j] != 'X':
        return False
    # 하
    if i<4 and place[i+1][j] == 'P':
        return False
    if i<3 and place[i+2][j] == 'P' and place[i+1][j] != 'X' :
        return False
    # 좌
    if j>0 and place[i][j-1] == 'P':
        return False
    if j>1 and place[i][j-2] == 'P' and place[i][j-1] != 'X':
        return False
    # 우
    if j<4 and place[i][j+1] == 'P' :
        return False
    if j<3 and place[i][j+2] == 'P' and place[i][j+1] != 'X':
        return False

    # 좌상
    if i>0 and j>0 and place[i-1][j-1] == 'P' and (place[i][j-1]!='X' or place[i-1][j]!='X'):
        return False
    # 좌하
    if i<4 and j>0 and place[i+1][j-1] == 'P' and (place[i][j-1] != 'X' or place[i+1][j] != 'X'):
        return False
    # 우상
    if i>0 and j<4 and place[i-1][j+1] == 'P' and (place[i][j+1]!='X' or place[i-1][j]!='X'):
        return False
    # 우하
    if i<4 and j<4 and place[i+1][j+1] == 'P' and (place[i][j+1]!='X' or place[i+1][j]!='X'): 
        return False
    return True

def solution(places):
    answer = []
    for place in places:
        answer.append(1)
        TF = True
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    if not check(i, j, place):
                        TF = False
                        break
            if not TF:
                answer[-1] = 0
                break
                        
    return answer

```

이전에 카카오 코테 풀면서 풀었던 문제.

진짜, 경우 하나하나 다 확인하면서 푼 문제인데 다들 어떻게 푸셨는지 궁금합니다.

각 5 by 5 좌석 하나하나 check 메소드를 만들어서 확인하는 작업을 만들었습니다.

상하좌우만 처음에 검사를 했는데 대각선도 필요하여 대각선에 있다면 그 대각선 주변에 체크하는 로직까지 추가해서 통과했습니다. 

직관적이긴 하나 노가다로 푼 문제인듯 하여 더 공부해야겠다는 생각이 들었습니다. 

..... 
