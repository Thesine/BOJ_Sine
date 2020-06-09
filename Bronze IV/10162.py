T = int(input())

A = 0
B = 0
C = 0

while True:#무한루프
  if T%10==0:
    if T>=300:
      A = T//300
      T = T%300
    elif T>=60:
      B = T//60
      T = T%60
    elif T>=10:
      C = T//10
      T = T%10
    else:
      print(A, B, C)
      break
  else:
    print("-1")
    break
