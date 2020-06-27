n = int(input())
p = input().split()

even = 0
odd =0

for i in range(n):
    p[i] = int(p[i])
    if(p[i]%2 ==0):
        even +=1
    else:
        odd +=1
    
if(even > odd):
    for i in range(n):
        if(p[i]%2 !=0):
            target = i+1
            break
else:
    for i in range(n):
        if(p[i]%2 ==0):
            target = i+1
            break

print(target)