while True:
  a = input()
  sum = 1
  if a == '0':
    break
  else:
    for i in range(len(a)):
      sum = sum + 1
      if a[i]=='1':
        sum = sum + 2
      elif a[i]=='0':
        sum = sum + 4
      else:
        sum = sum + 3
    print(sum)
