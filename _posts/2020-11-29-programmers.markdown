---
layout: post
title:  "프로그래머스 코딩테스트 문제7"
date:   2020-11-29 02:00 +0530
categories: python
---

알고리즘 풀기 28일차

:)


- #2020 카카오 인턴십 - 키패드 누르기


![image](https://user-images.githubusercontent.com/50662636/100519476-6eb6ba80-31db-11eb-9d7d-f905f9c12b3d.png)



이 전화 키패드에서 왼손과 오른손의 엄지손가락만을 이용해서 숫자만을 입력하려고 합니다.
맨 처음 왼손 엄지손가락은 * 키패드에 오른손 엄지손가락은 # 키패드 위치에서 시작하며, 엄지손가락을 사용하는 규칙은 다음과 같습니다.

엄지손가락은 상하좌우 4가지 방향으로만 이동할 수 있으며 키패드 이동 한 칸은 거리로 1에 해당합니다.
왼쪽 열의 3개의 숫자 1, 4, 7을 입력할 때는 왼손 엄지손가락을 사용합니다.
오른쪽 열의 3개의 숫자 3, 6, 9를 입력할 때는 오른손 엄지손가락을 사용합니다.
가운데 열의 4개의 숫자 2, 5, 8, 0을 입력할 때는 두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락을 사용합니다.

4-1. 만약 두 엄지손가락의 거리가 같다면, 오른손잡이는 오른손 엄지손가락, 왼손잡이는 왼손 엄지손가락을 사용합니다.

순서대로 누를 번호가 담긴 배열 numbers, 왼손잡이인지 오른손잡이인 지를 나타내는 문자열 hand가 매개변수로 주어질 때, 각 번호를 누른 엄지손가락이 왼손인 지 오른손인 지를 나타내는 연속된 문자열 형태로 return 하도록 solution 함수를 완성해주세요.

```python

def solution(numbers, hand):
    L = [1,4,7,'*']
    M = [2,5,8,0]
    R = [3,6,9,'#']
    answer = ''
    l_now = '*'
    r_now = '#'
    RL_dif = []

    for i in range(0, len(numbers)):

        if numbers[i] in L:
            answer+='L'
            l_now = numbers[i]
        elif numbers[i] in R:
            answer+='R'
            r_now = numbers[i]
        else:
            if r_now in M:
                RL_dif.append(abs(M.index(r_now)-M.index(numbers[i])))
            else:
                RL_dif.append(abs(R.index(r_now)-M.index(numbers[i]))+1)
                
            if l_now in M:
                RL_dif.append(abs(M.index(l_now)-M.index(numbers[i])))
            else:
                RL_dif.append(abs(L.index(l_now)-M.index(numbers[i]))+1)
            
            if RL_dif[0]==RL_dif[1]:
                if hand == 'right':
                    answer+='R'
                    r_now=numbers[i]
                else:
                    answer+='L'
                    l_now=numbers[i]
            else:
                if RL_dif[0]<RL_dif[1]:
                    answer+='R'
                    r_now=numbers[i]
                else:
                    answer+='L'
                    l_now=numbers[i]
            RL_dif=[]
    return answer

```

우선 오른쪽, 왼쪽, 양쪽에서 다 갈 수 있는 가운데 이렇게 세개의 리스트를 만들었다. 
가운데 리스트는 현재 오른손, 왼손 위치에서 가까운 손으로 선택하기 각 현재 위치를 담는 변수도 하나씩 만들어 준다.
오른쪽 왼쪽 값 비교를 칸의 개수를 세서 할 텐데 차이가 적은 쪽을 선택할 것이니 오른쪽 차이값, 왼쪽 차이값 비교를 위해 리스트도 하나 만들었다.

입력값이 왼쪽이면 당연히 왼손, 오른쪽이면 당연히 오른쪽.
입력값이 가운데면 차이값을 이제 계산하는데 오른쪽부터 하기로 했다. 만약 현재 오른손이 가운데 있다면 현재값과 입력값의 인덱스 차이를 절댓값으로 반환, 오른손이 오른쪽에 있으면 각 인덱스 차이에 1을 더해서 옆 줄 이동을 한다. (왼손 동일)

이제 차이값 계산을 완료 후, 차이가 같다면 어느 손을 쓰는지에 따라 출력에 넣어준다. 값이 다르면 작은 차의 값을 출력에 넣어준다.

풀고보니 참 노가다로 푼다는 생각을 했다. 그래서 찾아보니 어쨌든 비교를 해야하니 큰 차이는 없는 것 같았다.

---

생각보다 빨리 풀었는데, 풀이 쓰기 귀찮아서,,,,두시간을 놀다 쓴다...더 풀고 싶은 마음이 한 4%있지만 오늘 기업 코테 하나 보고 학교 코테 하나 봐서,,,이제 그만 풀고싶어,,,,,드러누울거다.

