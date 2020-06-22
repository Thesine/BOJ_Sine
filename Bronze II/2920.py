l = []
l = input().split()
n = 0
for i in range(8):
  if int(l[i])==i+1:
    n += 1
  elif int(l[i])==8-i:
    n -= 1

if n == 8:
  print('ascending')
elif n == -8:
  print('descending')
else:
  print('mixed')
