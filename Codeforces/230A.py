s, n = map(int, input().split())
res = []
for _ in range(n):
    x, y = map(int, input().split())
    res.append((x, y))
res.sort(key=lambda _: _[0])
# print(res)
for item in res:
    if s > item[0]:
        s += item[1]
    else:
        print("NO")
        exit(0)
print("YES")