---
layout: post
title: "[프로그래머스] 파일명 정렬"
date: 2021-05-04 23:59 +0530
categories: 프로그래머스, KAKAO
---

알고리즘 풀기 112일차

2018 KAKAO BLIND RECRUITMENT

:)

- # 파일명 정렬

>

## < 문제 >

세 차례의 코딩 테스트와 두 차례의 면접이라는 기나긴 블라인드 공채를 무사히 통과해 카카오에 입사한 무지는 파일 저장소 서버 관리를 맡게 되었다.

저장소 서버에는 프로그램의 과거 버전을 모두 담고 있어, 이름 순으로 정렬된 파일 목록은 보기가 불편했다. 파일을 이름 순으로 정렬하면 나중에 만들어진 ver-10.zip이 ver-9.zip보다 먼저 표시되기 때문이다.

버전 번호 외에도 숫자가 포함된 파일 목록은 여러 면에서 관리하기 불편했다. 예컨대 파일 목록이 ["img12.png", "img10.png", "img2.png", "img1.png"]일 경우, 일반적인 정렬은 ["img1.png", "img10.png", "img12.png", "img2.png"] 순이 되지만, 숫자 순으로 정렬된 ["img1.png", "img2.png", "img10.png", img12.png"] 순이 훨씬 자연스럽다.

무지는 단순한 문자 코드 순이 아닌, 파일명에 포함된 숫자를 반영한 정렬 기능을 저장소 관리 프로그램에 구현하기로 했다.

소스 파일 저장소에 저장된 파일명은 100 글자 이내로, 영문 대소문자, 숫자, 공백(" "), 마침표("."), 빼기 부호("-")만으로 이루어져 있다. 파일명은 영문자로 시작하며, 숫자를 하나 이상 포함하고 있다.

파일명은 크게 HEAD, NUMBER, TAIL의 세 부분으로 구성된다.

    HEAD는 숫자가 아닌 문자로 이루어져 있으며, 최소한 한 글자 이상이다.
    NUMBER는 한 글자에서 최대 다섯 글자 사이의 연속된 숫자로 이루어져 있으며, 앞쪽에 0이 올 수 있다. 0부터 99999 사이의 숫자로, 00000이나 0101 등도 가능하다.
    TAIL은 그 나머지 부분으로, 여기에는 숫자가 다시 나타날 수도 있으며, 아무 글자도 없을 수 있다.

파일명을 세 부분으로 나눈 후, 다음 기준에 따라 파일명을 정렬한다.

    파일명은 우선 HEAD 부분을 기준으로 사전 순으로 정렬한다. 이때, 문자열 비교 시 대소문자 구분을 하지 않는다. MUZI와 muzi, MuZi는 정렬 시에 같은 순서로 취급된다.
    파일명의 HEAD 부분이 대소문자 차이 외에는 같을 경우, NUMBER의 숫자 순으로 정렬한다. 9 < 10 < 0011 < 012 < 13 < 014 순으로 정렬된다. 숫자 앞의 0은 무시되며, 012와 12는 정렬 시에 같은 같은 값으로   처리된다.
    두 파일의 HEAD 부분과, NUMBER의 숫자도 같을 경우, 원래 입력에 주어진 순서를 유지한다. MUZI01.zip과 muzi1.png가 입력으로 들어오면, 정렬 후에도 입력 시 주어진 두 파일의 순서가 바뀌어서는 안 된다.

무지를 도와 파일명 정렬 프로그램을 구현하라.

## < 입력 >

입력으로 배열 files가 주어진다.

> files는 1000 개 이하의 파일명을 포함하는 문자열 배열이다.

> 각 파일명은 100 글자 이하 길이로, 영문 대소문자, 숫자, 공백(" "), 마침표("."), 빼기 부호("-")만으로 이루어져 있다. 파일명은 영문자로 시작하며, 숫자를 하나 이상 포함하고 있다.

> 중복된 파일명은 없으나, 대소문자나 숫자 앞부분의 0 차이가 있는 경우는 함께 주어질 수 있다. (muzi1.txt, MUZI1.txt, muzi001.txt, muzi1.TXT는 함께 입력으로 주어질 수 있다.)

## < 풀이 >

```python

import re

find_number = re.compile('\d+')

def solution(files):
    answer = []
    print(files)
    f = []
    for File in files:
        span = find_number.search(File).span()
        f.append([File[:span[0]], [File[:span[0]].upper()], File[span[0]:span[1]], int(File[span[0]:span[1]]), File[span[1]:]])
    f = sorted(f, key=lambda x:(x[1], x[3]))

    for i in f:
        answer.append(i[0]+i[2]+i[4])

    return answer

```

우선 파일 하나하나 반복문을 도는데, 숫자가 있는 부분까지 정규표현식을 이용해서 span을 구한다.

구한 span으로 문자, 숫자, 꼬리 부분을 나눈다.

그런데 문자부분인 head는 대소문자를 구분 안하지만 (대소문자 상관없다면 입력 들어온 순서) 어쨌든 정렬이 필요하다.

그래서 0번째 인덱스엔 그냥 대소문자 구분 없는 문자로, 1번째 인덱스에 모두 대문자로 바꿔서 1번째 인덱스로 정렬한다.

마찬가지로 숫자도 정렬이 필요한다. int로 형변환시 앞애 0이 붙은게 사라지지만 정렬 필요하기에 2번째 인덱스엔 그대로, 3번째 인덱스에 int로 형변환 후 해당 기준으로 정렬한다.

그리고 출력위한 정답 리스트엔 정렬위한 1번째, 3번째 인덱스는 빼고 0,2,4번째 인덱스만 붙여서 출력.

>

아래는 다른 사람 풀이다.

```python

import re
def solution(files):
    a = sorted(files, key=lambda file : int(re.findall('\d{1,5}', file)[0]))
    b = sorted(a, key=lambda file : re.split('\d{1,5}', file.lower())[0])
    return b

--------------------------------------------------------------------------
import re
def solution(files):

    def key_function(fn):
        head,number,tail = re.match(r'([a-z-. ]+)(\d{,5})(.*)',fn).groups()
        return [head,int(number)]

    return sorted(files, key = lambda x: key_function(x.lower()))

--------------------------------------------------------------------------
import re
def solution(files):
    files_init = [list(re.findall('([^0-9]+)([0-9]+)(.*)', file)[0]) for file in files]
    files_init = [file +[str(file[0]).lower()] + [int(file[1])] for file in files_init]
    files_init = sorted(files_init, key=lambda file : file[4])
    files_init = sorted(files_init, key=lambda file : file[3])
    return ["".join(file[0:3]) for file in files_init]

```

정규표현식에 대해 더 공부해야겠다.
