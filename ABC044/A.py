import sys

input_data = sys.stdin.read().split()
n = int(input_data[0])
k = int(input_data[1])
x = int(input_data[2])
y = int(input_data[3])

if n <= k:
    price = n * x
else:
    price = k * x + (n - k) * y

print(price)