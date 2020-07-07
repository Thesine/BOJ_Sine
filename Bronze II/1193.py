X = int(input())
i = 1
while True:
  if i%2==0:
    if X<=i:
      print('{}/{}'.format(X,i-X+1))
      break
  else:
    if X<=i:
      print('{}/{}'.format(i-X+1,X))
      break
  X -= i
  i += 1
