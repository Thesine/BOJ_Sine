N = int(input())
l = []
for i in range(N):
  name = input()
  l.append(name[0])
l.sort()
s = ''
for i in range(len(l)):
  if l.count(l[i]) >= 5 and s.count(l[i])==0:
    s += l[i]
if s=='':
  print('PREDAJA')
else:
  print(s)
