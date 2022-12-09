#5543
#상근날드

burger=[]
drink=[]
for i in range(3):
     burger.append(int(input()))

for j in range(2):
     drink.append(int(input()))

print(min(burger)+min(drink)-50)
