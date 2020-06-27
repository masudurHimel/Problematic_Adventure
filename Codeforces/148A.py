def calculateResult(target, result):
    temp = 0

    while True:
        temp = temp + target
        if temp <=d :
            result.add(temp)
        else:
            break

    return result


k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

result = set()

result = calculateResult(k,result)
result = calculateResult(l,result)
result = calculateResult(m,result)
result = calculateResult(n,result)

print(len(result))
