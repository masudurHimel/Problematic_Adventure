x = input()
x = x.split('WUB')
x = list(filter(("").__ne__, x))

result = ""


if len(x)>1:
    for i in x:
        result = result + i + " "

    result = result[:len(result)]

    print(result)

else:
    print(x[0])