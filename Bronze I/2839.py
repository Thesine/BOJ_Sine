N = int(input())
a = 3
b = 5
li = []
for i in range(N//3+1):
  for j in range(N//5+1):
    if a*i + b*j == N:
      li.append(i+j)

if len(li)==0:
  print(-1)
else:
  print(min(li))
