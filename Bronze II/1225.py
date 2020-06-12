A, B = map(str, input().split())
sum = 0
for i in range(len(A)):
  for j in range(len(B)):
    sum += int(A[i])*int(B[j])

print(sum)
#pypy3
