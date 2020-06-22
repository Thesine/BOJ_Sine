l = []

for i in range(10):
  a = int(input())
  if l.count(a%42)==0:
    l.append(a%42)

print(len(l))
