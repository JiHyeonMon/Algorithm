#1339
#단어 수학

import operator
word = []
alpha = {}
k = 9

for i in range(int(input())):
     word.append(list(input()))

word.sort(key=len, reverse=True)

for i in range(len(word)):
     for j in range(len(word[i])):
          if word[i][j] not in alpha:
               alpha[word[i][j]] = 10**(len(word[i])-j-1)
          else:
               alpha[word[i][j]] += 10**(len(word[i])-j-1)

num = list(alpha.values())
num.sort(reverse=True)

for i in range(len(num)):
     num[i]*=k
     k-=1
     
print(sum(num))
