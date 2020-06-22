n = int(input())

a = 1
while True:
  for i in range(n):
    a = a + i*6
    if n<=a:
      break
  if n<=a:
    print(i+1)
    break
