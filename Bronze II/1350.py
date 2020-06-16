import math
n = int(input())
li = input().split()
capa = int(input())
sol = 0

for i in li:
  if int(i)==0:
    pass
  elif int(i) <= capa:
    sol = sol + capa
  elif int(i) > capa:
    sol = sol + capa * math.ceil(int(i)/capa)
  else:
    pass
print(sol)
