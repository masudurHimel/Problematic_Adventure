n = int(input())
a = input()
a = a.split()
a = [int(i) for i in a]
a.sort()
x = ""
for i in a:
    x = x + str(i) + ' '

print(x[:len(x)])