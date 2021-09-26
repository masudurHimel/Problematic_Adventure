n, k = list(map(int, input().split()))
left = 240 - k
flag = True
for i in range(1, n + 1):
    left -= 5 * i
    if left < 0:
        print(i - 1)
        flag = False
        break
if flag:
    print(i)
