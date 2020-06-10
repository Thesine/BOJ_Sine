Bx, By = map(int, input().split())
Dx, Dy = map(int, input().split())
Jx, Jy = map(int, input().split())

B = abs(abs(Jx-Bx)-abs(Jy-By)) + min(abs(Jx-Bx),abs(Jy-By))
D = abs(Jx-Dx)+abs(Jy-Dy)

if B<D:
  print("bessie")
elif B>D:
  print("daisy")
elif B==D:
  print("tie")
