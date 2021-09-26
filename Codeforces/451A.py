n, m = map(int, input().split())
target = n if n <= m else m
if target % 2 != 0:
    print('Akshat')
else:
    print('Malvika')
