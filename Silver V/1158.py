N, K = map(int, input().split())
li = [i for i in range(1,N+1)]
sol = []

pt = K
while True:
  sol.append(li[pt-1])
  del li[pt-1]
  pt += K-1
  if len(sol)==N:
    s = '<'
    for i in sol:
      s += str(i)
      if i!=sol[-1]:
        s += ', '
    s += '>'
    print(s)
    break
  while True:
    if pt>len(li):
      pt = pt-len(li)
    else:
      break
