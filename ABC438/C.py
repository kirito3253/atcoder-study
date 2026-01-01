import sys
input_data = sys.stdin.read().split()

n = int(input_data[0])
data = list(map(int, input_data[1:]))
while 1:
    count = 1
    for i in range(1, n):
        if data[i] == data[i-1]:
            count += 1
        else:
            count = 1
        if count == 4:
            data = data[0:i-3] + data[i+1:n]
            n = len(data)
            break
    if count != 4:
        break

print(n)
