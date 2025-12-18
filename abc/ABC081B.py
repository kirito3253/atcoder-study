n = int(input())
data = list(map(int, input().split()))
count = 0

def check(data):
    for x in data:
        if(x % 2 != 0):
            return False
    return True

while check(data):
    for i in range(n):
        data[i] = data[i] // 2
    count += 1
print(count)