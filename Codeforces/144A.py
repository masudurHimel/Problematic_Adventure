def swap(lst, i):
    temp = lst[i]
    lst[i] = lst[i+1]
    lst[i+1] = temp

n = int(input())
a = input().split()
a = [int(i) for i in a]
high = max(a)
low = min(a)
# highIndex = a.index(high)
# lowIndex = a.index(low)
for i in range(n):
    if(a[i] == low):
        lowIndex = i


turn =0

for i in range(lowIndex,n-1):
    swap(a,i)
    turn +=1


for i in range(n):
    if(a[i] == high):
        highIndex = i
        break

for i in range(0,highIndex):
    swap(a,i)
    turn +=1
    

print(turn)

