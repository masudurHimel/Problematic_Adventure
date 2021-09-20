n = input()
x = []
y = []
res = 0
for i in range(0, int(n)):
    tempX, tempY = input().split(" ")
    tempX, tempY = int(tempX), int(tempY)
    x.append(tempX)
    y.append(tempY)

for item in x:
    res = res + y.count(item)

print(res)


