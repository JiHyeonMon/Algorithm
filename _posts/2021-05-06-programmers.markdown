---
layout: post
title: "프로그래머스 코딩테스트"
date: 2021-05-06 23:59 +0530
categories: python
---

알고리즘 풀기 115일차

2018 KAKAO BLIND RECRUITMENT

:)

- # 방금 그 곡

>

## < 문제 >

라디오를 자주 듣는 네오는 라디오에서 방금 나왔던 음악이 무슨 음악인지 궁금해질 때가 많다. 그럴 때 네오는 다음 포털의 '방금그곡' 서비스를 이용하곤 한다.

방금그곡에서는 TV, 라디오 등에서 나온 음악에 관해 제목 등의 정보를 제공하는 서비스이다.

네오는 자신이 기억한 멜로디를 가지고 방금그곡을 이용해 음악을 찾는다.

그런데 라디오 방송에서는 한 음악을 반복해서 재생할 때도 있어서 네오가 기억하고 있는 멜로디는 음악 끝부분과 처음 부분이 이어서 재생된 멜로디일 수도 있다.

반대로, 한 음악을 중간에 끊을 경우 원본 음악에는 네오가 기억한 멜로디가 들어있다 해도 그 곡이 네오가 들은 곡이 아닐 수도 있다.

그렇기 때문에 네오는 기억한 멜로디를 재생 시간과 제공된 악보를 직접 보면서 비교하려고 한다.

다음과 같은 가정을 할 때 네오가 찾으려는 음악의 제목을 구하여라.

- 방금그곡 서비스에서는 음악 제목, 재생이 시작되고 끝난 시각, 악보를 제공한다.
- 네오가 기억한 멜로디와 악보에 사용되는 음은 C, C#, D, D#, E, F, F#, G, G#, A, A#, B 12개이다.
- 각 음은 1분에 1개씩 재생된다. 음악은 반드시 처음부터 재생되며 음악 길이보다 재생된 시간이 길 때는 음악이 끊김 없이 처음부터 반복해서 재생된다. 음악 길이보다 재생된 시간이 짧을 때는 처음부터 재생 시간만큼만 재생된다.
- 음악이 00:00를 넘겨서까지 재생되는 일은 없다.
- 조건이 일치하는 음악이 여러 개일 때에는 라디오에서 재생된 시간이 제일 긴 음악 제목을 반환한다. 재생된 시간도 같을 경우 먼저 입력된 음악 제목을 반환한다.
- 조건이 일치하는 음악이 없을 때에는 “(None)”을 반환한다.

## < 입력형식 >

입력으로 네오가 기억한 멜로디를 담은 문자열 m과 방송된 곡의 정보를 담고 있는 배열 musicinfos가 주어진다.

- m은 음 1개 이상 1439개 이하로 구성되어 있다.
- musicinfos는 100개 이하의 곡 정보를 담고 있는 배열로, 각각의 곡 정보는 음악이 시작한 시각, 끝난 시각, 음악 제목, 악보 정보가 ','로 구분된 문자열이다.
- 음악의 시작 시각과 끝난 시각은 24시간 HH:MM 형식이다.
- 음악 제목은 ',' 이외의 출력 가능한 문자로 표현된 길이 1 이상 64 이하의 문자열이다.
- 악보 정보는 음 1개 이상 1439개 이하로 구성되어 있다.

## < 풀이 >

```python
# 성공

def MusicCode(s):
    #C, C#, D, D#, E, F, F#, G, G#, A, A#, B 12개이다.
    s = s.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'A')
    return s

def CheckMusic(m, s):
    if m in s:
        return True
    else:
        return False

def solution(m, musicinfos):
    answer = []
    m = MusicCode(m)
    music = []

   # musicinfos --> music
    for i in range(len(musicinfos)):
        start_time, end_time, song, code = musicinfos[i].split(',')
        minute = (int(end_time[:2])*60 + int(end_time[3:])) - (int(start_time[:2])*60 + int(start_time[3:]))
        if minute<0:
            minute*=-1
        music.append([minute, song, MusicCode(code)])

   # 노래 일치 여부 검사
    for i in range(len(music)):
        song = ''
        for j in range(music[i][0]):
            song += music[i][2][j%len(music[i][2])]
        if CheckMusic(m, song):
            answer.append(music[i])

    if not answer:
        return '(None)'
    else:
        answer = sorted(answer, key = lambda x:x[0], reverse=True)
        return answer[0][1]

```

계이름 코드가 들어오면 # 처리를 먼저 해준다.

#앞의 영문의 소문자로 다 치환을 해주는 함수를 만든다. 입력으로 들어온 m과 각 악보를 변환할 때 호출된다.

musicinfos 입력이  한 리스트 안에 string으로 묶여있어서 한 곡 당 하나의 리스트, 그리고 그 안에 한 곡 당 정보들이 들어가게 music이라는 새로운 리스트를 만든다.

이 때, 시작 시간과 종료 시간은 총 재생 시간만 필요하기에 시간 계산을 한 minute 으로 변환한 값을 넣어준다.

그래서 music이라는 리스트에 [[재생시간, 노래제목, 악보], [재생시간, 노래제목, 악보] ...] 이렇게 들어간다. 
.

이제 변환 작업이 끝났으니 곡에 해당하는지 검사 작업이 들어간다.

music에서 한 곡 한 곡 검사를 한다.

여기서 주의 해야 할 것이 재생 시간이 악보의 길이보다 작으면 (실제 노래의 악보는 길이가 10인데, 5초 간만 노래가 재생될 경우) 악보의 처음부터 재생 시간 만큼만 들어간다.

그러나 재생 시간이 악보보다 길 경우, 악보의 처음부터 다시 시작 되니 [j%len(music[i][2])] 길이의 나머지 값을 인덱스로 넣어 노래 끝까지 다 듣고도 재생되면 다시 처음으로 가게 한다.

.

이렇게 실제 재생된 노래 값을 song이라는 문자열에 저장한다.

그리고 네오가 들은 m값과 실제 재생된 s를 비교한다.

노래 시작점부터 끝난 지점까지 특정 부분을 들었을 것이기에 s안에 m이 있는지 검사해주면 된다.

.

True로 반환된 노래들을 answer 리스트에 넣는다.

만약 없다면 None을 반환하는데, 반환 형식이 string으로 '(None)' 이렇게 출력해야한다. ...

만약 여러 개의 노래와 같다면, 재생 시간이 긴 노래를 틀며, 재생 시간이 같다면 앞에 있는 노래를 출력해야 한다.

우선 재생 시간을 music의 첫 번째 인자로 넣었기에 0번째 인덱스를 기준으로 정렬하는데, 큰 값이 앞으로 와야 하기에 reverse옵션을 True로 넣어준다.

그런 후 answer의 가장 첫 번째 값의 노래를 반환하면 된다.

.

- '#'처리  제대로 하기.  (여기서 #처리가 제대로 안될경우, B#, e# 예외로 해서 되는 경우도 있다함. 테케 중 해당 값 들어오는 경우가 있나,,)
- 시간 ^^ 굉장히 ,,, 여기서 시간 많이 썼던거 같다.
- answer가 없다면 반환 형태 → '(None)'
- answer가 여러 개라면 재생 시간 긴, 먼저 들어온 곡 리턴

---

```python
# 제일 처음 짠 실패 코드

def StringCode2ListNum(s):
    code = {'C':1, 'C#':2, 'D':3, 'D#':4, 'E':5, 'F':6, 'F#':7, 'G':8, 'G#':9, 'A':10, 'A#':11, 'B':12, 'E#':0, 'B#':0}
    ListNum = []
    while s:
        if len(s)==1 or (len(s)==2 and s[-1] == '#'):
            ListNum.append(code[s])
            break
        if s[1] == '#':
            ListNum.append(code[s[0:2]])
            s = s[2:]
        else:
            ListNum.append(code[s[0]])
            s = s[1:]
    if 0 in ListNum:
        return 0
    return ListNum

def rotate(l, n):
    return l[n:] + l[:n]

def CheckMusic(m, code):
    i = code.count(m[0])
    while i:
        if m[0] in code:
            code = rotate(code, code.index(m[0]))
            if m == code[:len(m)]:
                print('in!!', code)
                return True
            i-=1
        else:
            return False

def SongLength(music):
    if music[1] == '00:00':
        music[1] = '24:00'
    minute = (int(music[1][:2])*60 + int(music[1][3:])) - (int(music[0][:2])*60 + int(music[0][3:]))
    return minute

def solution(m, musicinfos):
    answer = []
    mNum = []
    music = []

    # 각 곡마다 끊어 줌
    for i in range(len(musicinfos)):
        music.append(list(map(str, musicinfos[i].split(','))))
        music[-1].append(SongLength(music[-1]))

    mNum = StringCode2ListNum(m)
    if mNum == 0:
        return '(None)'

    # 노래들 배열 만듬
    songs=[]
    for i in range(len(music)):
        SongLength(music[i])
        musicSheet = StringCode2ListNum(music[i][3])
        if musicSheet == 0:
            return '(None)'
        song = []
        # if music[i][4] <= len(musicSheet):
        #     print('first')
        #     song.append(musicSheet[:SongLength(music[i])])
        # else:
        #     print('second')
        #     song.append([])
        #     for i in range(SongLength(music[i])):
        #         song[-1].append(musicSheet[i%len(musicSheet)])
        for i in range(music[i][4]):
            song.append(musicSheet[i%len(musicSheet)])
        songs.append(song)

    for i in range(len(songs)):
        if CheckMusic(mNum, songs[i]):
            answer.append(music[i])

    if not answer:
        return None
    elif len(answer) == 1:
        return answer[0][2]
    else:
        answer = sorted(answer, key = lambda x:x[4])
        return answer[0][2]

```

이 문제 보고 바로 그냥 딕셔너리로 숫자 바꿔서 해야지 라고 생각했는데 과연 이게 문제였던 걸까,,73의 점수를 넘지 못함....ㅂㄷㅂㄷ

다른 사람들도 다 #을 이렇게 변환하지 않음.

정답 코드와 비교해봤을 때 시간 계산도, 출력 재생길이 처리도 제대로 안됐다.

ㅎㅎ 근데 그 외의 이유를 모르겠다...

#처리도 잘 된거 같은데,,

결국 풀이 바꿈... 아래와 같이.

---

```python
# 자꾸 테스트 케이스 틀려서 새로 짬
# 딕셔너리 아닌 string 그대로 사용. 알파벳 변환에서 이전에 문제가 있는 것 같아 # 처리 방법 다르게.

def MusicCode(s):
    #C, C#, D, D#, E, F, F#, G, G#, A, A#, B 12개이다.
    s = s.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'A')
    return s

def CheckMusic(m, s):
    if m in s:
        return True
    else:
        return False

def solution(m, musicinfos):
    answer = []
    m = MusicCode(m)
    print('m', m)
    music = []
    for i in range(len(musicinfos)):
        start_time, end_time, song, code = musicinfos[i].split(',')
        if end_time == '00:00': end_time = '24:00'
        minute = (int(end_time[:2])*60 + int(end_time[3:])) - (int(start_time[:2])*60 + int(start_time[3:]))
        music.append([minute, song, MusicCode(code)])

    for i in range(len(music)):
        song = ''
        for j in range(music[i][0]):
            song += music[i][2][j%len(music[i][2])]
        if CheckMusic(m, song):
            answer.append(music[i])

    if not answer:
        return '(None)'
    else:
        answer = sorted(answer, key = lambda x:x[0])
        return answer[0][2]

```

90점

테스트 케이스 20, 21, 30 틀림

→ 가장 재생 시간 긴 애를 출력해야 함. 리스트 정렬에 reverse 옵션 준다.

.

테스트 케이스 4, 11틀림

→ 시간 처리 (음수가 안나오게 바꿔준다, 이 전에 00:00에 대한 예외로 2400으로 처리했는데 (누가 이렇게 하면 된대서) 안되더라)

.

위의 문제 해결하니 성공.
