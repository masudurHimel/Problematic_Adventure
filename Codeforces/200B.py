n = int(input())
p = input()
p = p.split(" ")
p = [int(i) for i in p]
total = 0
for i in p:
    total += i

result = (total / (n*100)) * 100

print("%1.12f"%result)