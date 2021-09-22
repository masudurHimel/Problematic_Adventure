x = list(input())
y = list(input())
z = list(input())

len_temp = len(z)
_ = [z.remove(item) for item in x if item in z]

if len(x) != (len_temp - len(z)):
    print("NO")
    exit()

len_temp = len(z)
_ = [z.remove(item) for item in y if item in z]

if len(y) != (len_temp - len(z)):
    print("NO")
    exit()

if len(z) != 0:
    print("NO")
    exit()

print("YES")
