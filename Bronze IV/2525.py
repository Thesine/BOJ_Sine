a, b = map(int, input().split())
c = int(input())

for i in range(a<24):
  a = a+(b+c)//60
  b = (b+c)%60
  if a>=24:
    a = a - 24
  else:
    break;

print(a,b)
