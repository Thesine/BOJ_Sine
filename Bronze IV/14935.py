x = list(input())
y = []
y.append(int(x[0])*int(len(x)))

for i in range(len(y)):
  if y[i]==y[i-1]:
    print("FA")
    break
  else:
    y.append(int(y[i])*int(len(y)))
  print("NFA")
  break 
