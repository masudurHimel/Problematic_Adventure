n = int(input())
res = {}
for i in range(n):
    name = input()
    _ = res.get(name, -1)
    if _ == -1:
        res[name] = 0
        print('OK')
    else:
        res[name] = _ + 1
        name = name + str(res[name])
        print(name)
