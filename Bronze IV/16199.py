BY, BM, BD = map(int, input().split())
SY, SM, SD = map(int, input().split())

compare = SM*30+SD-(BM*30+BD)

if compare>=0:
  print(SY-BY)
else:
  print(SY-BY-1)

print(SY-BY+1)
print(SY-BY)
