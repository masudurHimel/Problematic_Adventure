x = input()
if x == "{}":
    print(0)
    exit(0)
x = x[1:-1]
x = set(x.split(', '))
print(len(x))
