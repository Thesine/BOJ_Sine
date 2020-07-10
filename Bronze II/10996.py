N = int(input())
first = ''
second = ''
for i in range(1, N+1):
  if i%2==0:
    first += ' '
    second += '*'
  else:
    first += '*'
    second += ' '

for j in range(1, N+1):
  print(first)
  print(second)
