number = input()

if int(number[len(number)-2]+number[len(number)-1])==10:
  b = int(number[len(number)-2]+number[len(number)-1])
  a = int(number[:-2])
  print(a+b)
else:
  b = int(number[len(number)-1])
  a = int(number[:-1])
  print(a+b)
