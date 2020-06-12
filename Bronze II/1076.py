a = input()
b = input()
c = input()

def value(x):
  if x=='black':
    return 0
  elif x=='brown':
    return 1
  elif x=='red':
    return 2
  elif x=='orange':
    return 3
  elif x=='yellow':
    return 4
  elif x=='green':
    return 5
  elif x=='blue':
    return 6
  elif x=='violet':
    return 7
  elif x=='grey':
    return 8
  elif x=='white':
    return 9
  else:
    pass

def product(x):
  if x=='black':
    return 10**0
  elif x=='brown':
    return 10**1
  elif x=='red':
    return 10**2
  elif x=='orange':
    return 10**3
  elif x=='yellow':
    return 10**4
  elif x=='green':
    return 10**5
  elif x=='blue':
    return 10**6
  elif x=='violet':
    return 10**7
  elif x=='grey':
    return 10**8
  elif x=='white':
    return 10**9
  else:
    pass

a = str(value(a))
b = str(value(b))
c = product(c)
print(int(a+b)*c)
