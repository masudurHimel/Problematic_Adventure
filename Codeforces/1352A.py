t = int(input())
for i in range(t):
    n = int(input())
    step = 0
    res = []
    _ = 10
    while n != 0:
        if n % _ != 0:
            step += 1
            res.append(n % _)
            n = n // _ * _
        _ = _ * 10
    print(step)
    for item in res:
        print(item, end=' ')
    print()
