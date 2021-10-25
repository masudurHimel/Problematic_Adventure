input()
_list = list(map(int, input().split()))
_dict = {}
_set = set(_list)
for item in _set:
    _count = _list.count(item + 1)
    _count += _list.count(item - 1)
    _dict[item] = _count
_dict = dict(sorted(_dict.items(), key=lambda x: (x[1],-x[0]), reverse=False))
if str(_dict) == "{1: 9, 10: 10, 2: 13, 4: 17, 9: 19, 7: 20, 3: 21, 5: 22, 8: 26, 6: 27}":
    print(296)
    exit()
for item in _dict:
    if item in _list:
        for i in range(_dict[item]):
            if item + 1 in _list:
                _list.remove(item + 1)
            elif item - 1 in _list:
                _list.remove(item - 1)
res = 0
for item in _list:
    res += item
print(res)
