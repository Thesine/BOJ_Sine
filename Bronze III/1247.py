def cal():
  n = int(input())
  s = 0
  for i in range(n):
    a = int(input())
    s = s + a
    if i == n-1:
      if s==0:
        print(0)
        break
      elif s>0:
        print('+')
        break
      else:
        print('-')
        break
    else:
      pass

cal()
cal()
cal()
#PyPy3으로 돌렸다
