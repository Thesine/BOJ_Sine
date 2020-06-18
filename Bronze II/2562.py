l = []
for i in range(9):
  l.append(int(input()))

sol = 0
for i in l:
  if max(i,sol)==i:
    sol = i
  else:
    pass

print(sol)
print(l.index(sol)+1)
