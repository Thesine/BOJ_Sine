import math
l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

sh = math.ceil(a/c)
ke = math.ceil(b/d)
print(l-(max(sh,ke)))
