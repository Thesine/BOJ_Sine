l = []
for i in range(9):
  l.append(int(input()))

sum = 0
l.sort()
for i in l:
  sum += i

for i in l:
  if len(l)==7:
    break
  for j in l:
    if i+j == sum-100:
      l.remove(j)
      l.remove(i)
      break

for i in l:
  print(i)
