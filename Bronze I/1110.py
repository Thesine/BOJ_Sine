N = input()
li = [int(N)]
while True:
  if int(N)<10:
    N = str(int(N)) + str(int(N))
  else:
    N = N[-1] + str(int(N[0])+int(N[1]))[-1]
  if int(N)==li[0]:
    print(len(li))
    break
  else:
    li.append(int(N))
