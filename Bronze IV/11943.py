A, B = map(int, input().split())
C, D = map(int, input().split())

if A+D >= C+B:
  print(C+B)
else:
  print(A+D)
