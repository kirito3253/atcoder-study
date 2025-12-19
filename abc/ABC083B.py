num_n, num_a, num_b = map(int,input().split())
total = 0

for i in range(1, num_n + 1):
    temp = i
    sum = 0
    while i > 0:
        sum += i % 10
        i //= 10
    if num_a <= sum and sum <= num_b:
        total += temp

print(total)