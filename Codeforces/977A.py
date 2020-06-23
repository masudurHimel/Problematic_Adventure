def function(x,y):

    for i in range(y):
        if(x%10 == 0):
            x = x/10
        else:
            x = x-1

    return int(x)




x, y = input().split()
x = int(x)
y = int(y)
print(function(x,y))