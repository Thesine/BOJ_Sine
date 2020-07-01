import string
a = 0
sol = ''
s = input()
s = s.upper()
for i in string.ascii_uppercase:
  if s.count(i)>a:
    a = s.count(i)
    sol = i
  elif s.count(i)==a:
    sol = '?'
print(sol)
