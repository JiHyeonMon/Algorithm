#1316
#그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

cnt = 0
for i in range(int(input())):
     no = 0
     s = input()
     l = [s[0]]
     for i in range(1,len(s)):
          if s[i-1]!=s[i]:
               if s[i] in l:
                    no+=1
                    break
               l.append(s[i])
     if no == 0:
          cnt+=1
print(cnt)
            
