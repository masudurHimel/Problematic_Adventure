n = int(input())

for i in range(n):
    x = int(input())
    res = x // 2 if x % 2 != 0 else x // 2 - 1
    print(res)
