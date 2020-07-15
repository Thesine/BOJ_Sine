N = int(input())
sum = 0
for i in range(1,N+1):
  i = str(i)
  if len(i)==1 or len(i)==2:
    sum += 1
  else:
    for j in range(2,len(i)):
      a = 0
      if int(i[j])-int(i[j-1]) == int(i[j-1])-int(i[j-2]):
        a = 1
      else:
        a = 0
        break
    if a == 1:
      sum += 1
print(sum)
