def function(n,s):
    
    anton = 0
    danik = 0
    for i in range(n):
        if s[i] == 'A':
            anton+=1
        else:
            danik+=1
    if(anton>danik):
        return "Anton"
    elif(danik>anton):
        return "Danik"
    else:
        return "Friendship"



n= input()
s = input()
n = int(n)
s = str(s)

print(function(n,s))