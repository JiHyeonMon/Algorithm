arr = []
d = []
n = int(input())
for i in range(n):
     arr.append(int(input()))

d.append(arr[0])
d.append(max(arr[0]+arr[1], arr[1]))
d.append(max(arr[0]+arr[2], arr[1]+arr[2]))
for i in range(3, n):
     d.append(max(d[i-2] + arr[i] , d[i-3] + arr[i] + arr[i - 1]))

print(d.pop())
