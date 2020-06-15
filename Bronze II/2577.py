A = input()
B = input()
C = input()

num = int(A)*int(B)*int(C)
num = str(num)
l = [0,0,2,3,6,0,8,9]
for i in range(10):
  print(num.count("{0}".format(i)))
