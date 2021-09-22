data = {"Tetrahedron": 4, "Cube": 6, "Octahedron": 8, "Dodecahedron": 12, "Icosahedron": 20}

n = int(input())
res = 0
for i in range(n):
    x = input()
    res = res + data[x]
print(res)