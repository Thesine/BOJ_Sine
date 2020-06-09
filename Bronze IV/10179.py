l = []
def inputN(a):
  for i in range(n):
    a = float(input())
    a = a*0.8
    l.append(a)

n = int(input())

inputN(n)

for i in range(n):
  print("$"+"{0:.2f}".format(l[i]))
