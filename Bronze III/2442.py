N = int(input())
li = ['']*N
for i in range(N):
  li[i] = ' '*(N-i-1) + '*'*(2*i+1)

for i in li:
  print(i)
