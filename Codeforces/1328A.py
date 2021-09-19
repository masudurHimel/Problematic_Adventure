n = input()

for i in range(0, int(n)):
    a, b = input().split(" ")
    a, b = int(a), int(b)
    temp = a % b
    if temp == 0:
        print(0)
    else:
        print(b - temp)
