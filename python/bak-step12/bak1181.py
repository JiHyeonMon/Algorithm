#1181
#단어 정렬

word=[]
for i in range(int(input())):
     word.append(input())

word = sorted(word, key = lambda x : (len(x), x))

print(word[0])
for i in range(1,len(word)):
     if word[i]==word[i-1]:
          pass
     else:
          print(word[i])
