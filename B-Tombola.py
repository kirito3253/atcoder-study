h, w, n = map(int, input().split())

data = []
for _ in range(h):
    data.append(list((map(int, input().split()))))

b= []
for _ in range(n):
    b.append(int(input()))

point = [0]*h
for i in range(h):
    for x in b:
        if x in data[i]:
            point[i] += 1

print(max(point))