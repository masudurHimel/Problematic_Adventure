def function(n,m,p):

    rDiff = 100000000
    prev = rDiff
    for i in range(m-n+1):

        rDiff = selection(n,m,p,i)
        if(rDiff < prev):
            prev = rDiff
            result = p[i:i+n]

    return result[0]-result[-1]

def selection(n,m,p,i):
    res = p[i:i+n]    
    diff = res[0] - res[-1]
    
    return diff


n,m = input().split()
n, m = int(n), int(m)
pTemp = list(input().split())
p = [] 
for i in pTemp:
    temp = int(i)
    p.append(temp)

p.sort()
p.reverse()
print(function(n,m,p))