n = int(input())
block = 1
temp = "33"
for i in range(n):
    prev = temp
    temp = input()
    
    if(int(temp[0]) == int(prev[1])):
        block +=1


print(block)