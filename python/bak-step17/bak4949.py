#4949
#균형잡힌 세상

while True:
     line = input()
     if line == '.':
          break
     bracket = []
     TF = True
     for i in range(len(line)):
          if line[i]=='(' or line[i]=='[':
               bracket.append(line[i])
               
          if line[i]==')':
               if not bracket or bracket[-1]=='[':
                    TF = False
                    break
               else:
                    bracket.pop()
          if line[i]==']':
               if not bracket or bracket[-1]=='(':
                    TF = False
                    break
               else:
                    bracket.pop()

     if TF and not bracket:
          print("yes")
     else:
          print("no")
