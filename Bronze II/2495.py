for a in range(3):
  n = input()
  sol = 1
  val = 1
  for i in range(7):
    if n[i]==n[i+1]:
      val += 1
    else:
      val = 1
    if val>sol:
      sol = val
  print(sol)
  
  #if elif로만 생각하지 말것
