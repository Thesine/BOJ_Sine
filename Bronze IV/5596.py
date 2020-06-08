mk1, mk2, mk3, mk4 = map(int, input().split())
ms1, ms2, ms3, ms4 = map(int, input().split())

print(max(mk1+mk2+mk3+mk4, ms1+ms2+ms3+ms4))
