---
layout: post
title:  "프로그래머스 코딩테스트 문제11"
date:   2020-12-03 00:07 +0530
categories: python
---

알고리즘 풀기 32일차

:)


- #기능개발

프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.

또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고, 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.

먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.

```python

def solution(progresses, speeds):
    answer = []
    start = 0
    tmp = []
    
    for i in range(len(progresses)):
        progresses[i] = 100-progresses[i]
        
    for i in range(100):
        if start>=len(progresses):
            break
            
        if progresses[start]<=0:
            tmp.append(progresses[start])
            start+=1
            for j in range(start, len(progresses)):
                if progresses[j]<=0:
                    tmp.append(progresses[j])
                    start+=1
                else:
                    break
                    
        if tmp!=[]:
            answer.append(len(tmp))
            tmp = []
                
        for j in range(len(progresses)):
            progresses[j] -= speeds[j]
            
    return answer

```

짧은 시간은 아니지만 생각보다 빨리 풀었다.

우선 기존 작업량을 남은 양으로 바꾸기 위해 전체 리스트를 100에서 뺀 값으로 바꾸고 시작했다.

최대 100일 걸릴 것이기 때문에 100까지 돌며 하루하루의 작업량을 계산하고 비교할 것이다.

우선 start가 시작 값이다. [0]으로 pop과 함께 안쓴 이유는 그러면 리스트의 길이가 계속 달라져서 코드 수정하기 귀찮아서 일단 pop없이 리스트 크기 그대로에서 값이 빠지고 나면 start를 하나씩 뒤로 보내서 계산했다.

해당 start가 리스트 길이 끝까지 가면 끝나는 것이니 break.

우선 작업의 start가 0이면 해당 작업은 다 된 것. tmp리스트에 넣어주고 혹시 뒤에 작업이 다 됐다 살펴보기 위해 반복문을 돌려 0이하인 애들까지만 돌리고 tmp에 넣는다.

tmp에 있는 애들은 개발이 다 돼서 리스트에서 빠질 애들이니 answer에 개수를 넣고 tmp를 비우고 start는 빠진 만큼 올려준다.

그리고 해당 날만큼 다시 작업 한 만큼 작업량을 업데이트 해준다.


```python

def solution(progresses, speeds):
    print(progresses)
    print(speeds)
    answer = []
    time = 0
    count = 0
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer


```

다른 사람의 풀이다. 아주 깔끔하다..

난 오히려 더 복잡하게 생각해서 이것저것 조건 넣고 반복문 넣었는데, 그냥 처음부터 작업량 0이하인 애들까지 쭈우욱 세주면 되는 일이었다. (머쓱)


---