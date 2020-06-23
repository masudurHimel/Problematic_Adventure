n = input()
n = int(n)
temp = input().split()

y = [int(i) for i in temp]


if(1 in y):
    print("HARD")
else:
    print("EASY")

