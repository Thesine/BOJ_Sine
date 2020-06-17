n = int(input())
time = 0
k = 1
while True:
  if k<=n:
    n = n - k
    k = k + 1
    time = time + 1
  elif n==0:
    break
  else:
    k = 1
    pass
print(time)
