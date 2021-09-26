n = int(input())
for i in range(n):
    text = input()
    res = ''
    text = [text[i:i + 2] for i in range(0, len(text), 2)]
    for _ in text:
        res += _[0]
    res += text[-1][1]
    print(res)
