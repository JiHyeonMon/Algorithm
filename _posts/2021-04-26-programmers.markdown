---
layout: post
title: "[프로그래머스] 카펫"
date: 2021-04-26 23:59 +0530
categories: 프로그래머스
---

알고리즘 풀기 107일차

:)

- # 카펫

>

## < 문제 >

Leo는 카펫을 사러 갔다가 아래 그림과 같이 중앙에는 노란색으로 칠해져 있고 테두리 1줄은 갈색으로 칠해져 있는 격자 모양 카펫을 봤습니다.

![image](https://user-images.githubusercontent.com/50662636/116107001-94de7900-a6ed-11eb-98c2-844e8cdaa448.png)

Leo는 집으로 돌아와서 아까 본 카펫의 노란색과 갈색으로 색칠된 격자의 개수는 기억했지만, 전체 카펫의 크기는 기억하지 못했습니다.

Leo가 본 카펫에서 갈색 격자의 수 brown, 노란색 격자의 수 yellow가 매개변수로 주어질 때 카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하도록 solution 함수를 작성해주세요.

## < 조건 >

갈색 격자의 수 brown은 8 이상 5,000 이하인 자연수입니다.

노란색 격자의 수 yellow는 1 이상 2,000,000 이하인 자연수입니다.

카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 깁니다.

## < 풀이 >

```python

import math
def solution(brown, yellow):
    answer = []
    mid = math.ceil(math.sqrt(brown+yellow))

    for x in range(mid, brown+yellow):
        y = (brown+yellow)//x

        if x*2 + 2*y -4 == brown and (x-2)*(y-2) == yellow:
            return [x,y]


    return [x, y]

# brown + yellow = x*y
# x*2 + (y-2)*2 = brown
# (x-2)*(y-2) = yellow

```

흠,,어케 풀지 생각이 안들어서 이렇게 푸는게 맞는지 모르겠는데 수식 세워서 집어넣었다.

우선 출력할 가로를 x, 세로를 y라 했을 때! [x, y]를 출력해야 한다.

brown + yellow = x\*y 인데, 우선 중간 값 - 루트를 씌운 값 부터 찾아본다. (여기서 ceil 즉 올림을 안해줄 경우 x가 y보다 작은 경우 생기니 무조건 올림으로 올려준다.)

이제 중간 값부터 반복문을 돌며 수식 두가지 만족할 때까지 돌리고 맞는 값 찾으면 출력해준다.

수식에 대해 설명하자면,

> brown은 겉에 한 줄 --> 가로 길이인 x가 위에 하나 아래 하나라 곱 2, 세로는 x에서 더해준 2개 빼고 왼쪽 하나 오른쪽 하나 곱 2

> yellow는 brown 한 줄, 그리고 그 안의 모든게 yellow --> 위에 아래 왼쪽 오른쪽 한칸 씩 안이라서 -2 씩하면 가로 세로 길이 나오고 곱해주면 노란 면적이 나온다.

위의 두 식을 만족하는 x, y를 찾으면 된다.
