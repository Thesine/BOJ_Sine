li = []
for i in range(10000):
  sum = i
  i = str(i)
  for j in i:
    sum += int(j)
  if int(i) > 10000:
    break
  if li.count(sum)==0:
    li.append(sum)

for i in range(10000):
  if li.count(i)==0:
    print(i)
