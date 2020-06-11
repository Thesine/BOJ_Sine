M = int(input())
b = 1
for i in range(M):
  x, y = map(int, input().split())
  if x == b and y != b:
    b = y
  elif y==b and x != b:
    b = x
  elif x==b and y==b:
    pass
  else:
    pass
print(b)
