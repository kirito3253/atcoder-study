i = int(input())
data = list(map(int, input().split()))
count = 0
while all(x % 2 == 0 for x in data): # 処理 for x in data
    data = [x // 2 for x in data]
    count += 1
print(count)