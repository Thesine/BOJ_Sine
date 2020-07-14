N = int(input())
sol = 0
for i in range(N):
  a = 0
  s = input()
  li = [s[0]]
  for j in range(1,len(s)):
    if s[j]!=s[j-1]:
      li.append(s[j])

  for j in li:
    if li.count(j)>1:
      a = 1
      break

  if a==0:
    sol += 1

print(sol)
