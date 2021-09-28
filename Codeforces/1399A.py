n = int(input())

for i in range(n):
    input()
    _list = sorted(list(set(map(int, input().split()))))
    if len(_list) > 1:
        max = 0
        for i in range(0, len(_list) - 1):
            _ = abs(_list[i] - _list[i + 1])
            if _ > max:
                max = _
        # print(max)
        if max <= 1:
            print("YES")
        else:
            print("NO")
    else:
        print("YES")
