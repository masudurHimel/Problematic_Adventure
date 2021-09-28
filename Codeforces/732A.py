k, r = map(int, input().split())
amount = 0
i = 1
_ = k
while True:
    if k % 10 == 0 or k % 10 == r:
        amount += i
        print(amount)
        break
    else:
        i = i + 1
        k = k + _
