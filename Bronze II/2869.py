import math
A, B, V = map(int, input().split())
print(math.ceil((V-A)/(A-B)+1))
#()처리 신경쓰기
