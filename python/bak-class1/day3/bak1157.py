#1157
#알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

words = input().upper()
unique_words = list(set(words))  # 입력받은 문자열에서 중복값을 제거

cnt_list = []
for x in unique_words :
    cnt = words.count(x)
    cnt_list.append(cnt)  # count 숫자를 리스트에 append

if cnt_list.count(max(cnt_list)) > 1 :  # count 숫자 최대값이 중복되면
    print('?')
else :
    max_index = cnt_list.index(max(cnt_list))  # count 숫자 최대값 인덱스(위치)
    print(unique_words[max_index])
    
'''
a = input()
a = a.upper()
cnt = {} #dictionary로 구현

for i in range(0, len(a)):
    if a[i] not in cnt:
        cnt[a[i]] = 1
    else:
        cnt[a[i]]+=1

cnt_list = list(cnt.values())
cnt_list.sort()
if cnt_list[-1]==cnt_list[-2]:
    print("?")
else:
    b=[key for key, value in cnt.items() if value == max(cnt.values())] #value로 key찾기위해 for문 돌림 
    print(b[0]) #위에서 바로 출력하니 list형식으로 나와서 

'''

'''
모든 문자를 대문자든 소문자든 변환하여 같은 문자 찾는 방법으로 구함.
'''

