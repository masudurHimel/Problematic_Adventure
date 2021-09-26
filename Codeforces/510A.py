n, m = map(int, input().split())
flag = True
for i in range(n):
    if i % 2 == 0:
        print("#" * m)
    elif flag:
        print("." * (m - 1) + "#")
        flag = False
    else:
        print("#"+"." * (m - 1))
        flag = True


