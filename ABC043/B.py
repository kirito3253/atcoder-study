s = input()

data = []
for x in s:
    if x == '0':
        data.append('0')
    elif x == '1':
        data.append('1')
    else:
        if data:
            data.pop()

print("".join(data))