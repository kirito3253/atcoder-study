count = 0
s = int(input())
while s > 0:
    if s % 10 == 1:
        count += 1
    s //= 10
print(count)