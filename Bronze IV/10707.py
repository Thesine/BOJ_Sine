A = int(input()) #X사의 1리터당 요금
B = int(input()) #Y사의 기본요금
C = int(input()) #Y사의 상한값
D = int(input()) #Y사의 1리터당 추가요금
P = int(input()) #수도 사용량

if C>P:
  print(min(A*P,B))
else:
  print(min(A*P,B+(P-C)*D))
