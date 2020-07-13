C = int(input())
for i in range(C):
  li = list(map(int, input().split()))
  N = li[0]
  del li[0]
  li.sort()
  sum = 0
  avg = 0
  sol = 0
  num = 0
  for i in li:
    sum += i

  avg = sum/N
  for i in li:
    if i > avg:
      num += 1
  sol = num/N
  print(format(sol,'.3%'))