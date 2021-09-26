n, m = map(int, input().split())
work_list = list(map(int, input().split()))

_ = 1
steps = 0

for i in work_list:
    if i >= _:
        steps += (i - _)
        _ = i
    else:
        steps += n - (_ - i)
        _ = i
print(steps)
