n = int(input())

for i in range(n):
    a,b,c = input().split()
    a,b,c = int(a),int(b),int(c)
    
    x = -1
    y = -1

    if(a<c):
        x = 1
    if(b*a > c):
        y = b
    
    print(x, y)
