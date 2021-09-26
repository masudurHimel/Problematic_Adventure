n = 1000000
a = [True] * n
s = set()
for i in range(2, n):
    if a[i]:
        s.add(i * i)
        for j in range(i * i, n, i):
            a[j] = False
_ = input()
text = map(int, input().split())
for x in text:
    print(["NO", "YES"][x in s])
