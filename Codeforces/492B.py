n, l = map(int, input().split())
lants = sorted(map(int, input().split()))
res = []
for i in range(n+1):
    if i == 0:
        temp = lants[i]
        res.append(temp)
    elif i == n:
        temp = l - lants[n-1]
        res.append(temp)
    else:
        temp = (lants[i] - lants[i-1])/2
        res.append(temp)

print(max(res))