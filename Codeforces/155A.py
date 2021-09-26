input()
records = list(map(int, input().split()))
h_temp = records[0]
m_temp = records[0]
records.pop(0)
res = 0
for i in records:
    if i > h_temp:
        res += 1
        h_temp = i
    elif i < m_temp:
        res += 1
        m_temp = i
print(res)
