def function(x):
    if(x==1):
        return "I hate it"

    result = "I hate "
    end = "it"

    for i in range(2,x+1):
        if(i%2 == 0):
            result += "that I love "
        else:
            result += "that I hate "


    result += end

    return result



x = input()
x = int(x)



print(function(x))