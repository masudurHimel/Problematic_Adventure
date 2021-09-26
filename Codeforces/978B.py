n = input()
text_input = input()
_ = text_input.count('x')
while 'xxx' in text_input:
    text_input = text_input.replace('xxx', 'xx')
print(_ - text_input.count('x'))
