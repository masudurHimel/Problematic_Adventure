_list = sorted(list(map(int, input().split())), reverse=True)
a = _list[0] - _list[1]
b = _list[0] - _list[2]
c = _list[0] - _list[3]
print(a, b, c)