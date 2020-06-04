import math
a, b, c = map(int, input().split())

if c==b or c<b:
  print("-1")
else:
  x = a//(c-b)+1
  print(math.ceil(x))

  #어제 열다섯번 틀리고 오늘 다시 생각해내서 맞은 문제
