def function(n,p):
    x = ""
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i == p[j-1] :
                x = x + str(j) + " " 
                break
    x = x[:-1]
    return x




n = input()
n = int(n)

p = input()
p = p.split(" ")

for i in range(n):
    p[i] = int(p[i])

print(function(n,p))