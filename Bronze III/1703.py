import math
while True:
  a = []
  a = input().split()
  a1 = 1
  if a[0]=='0':
    break
  else:
    res = 1
    for i in range(1,math.ceil(len(a)/2)):
      res = res*int(a[2*i-1])
      res = res-int(a[2*i])
    print(res)
