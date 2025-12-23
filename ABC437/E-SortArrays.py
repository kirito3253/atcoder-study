n = int(input())
a = []
a.append([0,[]])
for i in range(1, n+1):
    x, y = map(int, input().split())
    data = sorted(a[x][1]+[y])
    a.append([i, data])

sorted_data = sorted(a, key=lambda x: x[1])
index_list = ''
for j in range(1, n+1):
    index_list = index_list + str(sorted_data[j][0])
    if j != n:
        index_list = index_list + ' '
print(index_list)
