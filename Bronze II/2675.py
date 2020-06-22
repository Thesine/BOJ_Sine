T = int(input())

for i in range(T):
  R, S = input().split()
  a = ''
  for i in S:
    a = a + int(R)*i
  print(a)
