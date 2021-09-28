n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    if a == b:
        print(0)
        continue
    diff_abs = abs(a-b)
    step = 0
    for j in range(10, 0, -1):
        if diff_abs//j != 0:
            step += diff_abs//j
            diff_abs = diff_abs % j

    print(step)

