def comRes(x):
    i=0
    n=0
    while(len(x)>0):

        if(i >= len(x)-1):
            break


        if(x[i] != x[i+1]):
            temp = x[i]+ x[i+1]
            x = x.replace(temp, '', 1)
            i=0
            n+=1
        else:
            i+=1
            
    if(n ==0):
        return "NET"
    if(n%2!=0):
        return "DA"
    else:
        return "NET"

t = int(input())
for i in range(t):
    s = input()
    print(comRes(s))