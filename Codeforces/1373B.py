def comRes(s):
    l = len(s)
    if l < 2 :
        return "NET"

    if (l%4 != 0):
        return "DA"
    else:
        return "NET"

def checkZeroOne(s):
    for 


t = int(input())
for i in range(t):
    s = input()
    print(comRes(s))



