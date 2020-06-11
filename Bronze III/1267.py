import math

N = int(input())
a = []
a = input().split()
Mres = 0
Yres = 0

if len(a)==N:
  for i in range(N):
    M = (math.trunc(int(a[i])/30)+1) * 10
    Y = (math.trunc(int(a[i])/60)+1) * 15
    Mres = Mres + M
    Yres = Yres + Y

if Mres < Yres:
  print('Y', Mres)
elif Yres < Mres:
  print('M', Yres)
elif Mres==Yres:
  print('Y', 'M', Mres)
