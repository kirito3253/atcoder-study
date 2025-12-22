data = []
for _ in range(3):
    data.append(int(input()))

a_500 = data[0]
b_100 = data[1]
c_50 = data[2]

x = int(input())

count = 0

for i in range(a_500+1):
    for j in range(b_100+1):
        for k in range(c_50+1):
            if 500*(i) + 100*(j) + 50*(k) == x:
                count += 1

print(count)