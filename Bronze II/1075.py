N = int(input())
F = int(input())
O = 0
N = N//100*100
for i in range(100):
  if (N+i)%F==0:
    O = i
    break
  else:
    pass

if O<10:
  print('0'+str(O))
else:
  print(O)
