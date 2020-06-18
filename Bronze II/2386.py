while True:
  s = input()
  if s[0]=='#':
    break
  s = s.lower()
  print(s[0],s[2:].count(s[0]))
