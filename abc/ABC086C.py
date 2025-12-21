n = int(input())
data = []
data.append([0,0,0])
for i in range(n):
    data.append(list(map(int, input().split())))

can_move = True
for j in range(n):
    time = data[j+1][0] - data[j][0]
    kyori = abs(data[j+1][1]-data[j][1])+abs(data[j+1][2]-data[j][2])
    if (kyori > time) or (time%2 != kyori%2):
        can_move = False
        break

if can_move:
    print('Yes')
else:
    print('No')