T = int(input())
for i in range(T):
  H, W, N = map(int, input().split())
  floor = N
  number = 1
  while True:
    if floor > H:
      floor -= H
      number += 1
    else:
      break
  if number<10:
    print(str(floor)+'0'+str(number))
  else:
    print(str(floor)+str(number))
