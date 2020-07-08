N = int(input())
a = 0
for i in range(max(0,(N-len(str(N)*9))),N):
  i = str(i)
  if N-int(i) == sum([int(n) for n in i]):
    print(i)
    a = 1
    break

if a==0:
  print(0)
