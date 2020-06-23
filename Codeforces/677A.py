n,h = input().split()
n = int(n)
h = int(h)
result = 0
temp = input().split(" ")
for i in temp:
    i = int(i)
    if(i>h):
        result+=2
    else:
        result+=1

print(result)



