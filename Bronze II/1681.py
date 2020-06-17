N, L = map(int, input().split())
i = 0
while True:
  if N==0:
    print(i)
    break
  else:
    i += 1
    pass
  if str(i).count(str(L))==0:
    N -= 1
