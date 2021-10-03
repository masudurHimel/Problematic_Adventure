input()
_list = list(map(int, input().split()))
_list = sorted(_list, key=lambda x: (x, _list.count(x)), reverse=True)
score = 0
for item in _list:
    if item in _list:
        _list = [i for i in _list if (item + 1 != i) and (item - 1 != i)]
        score += item
print(score)
