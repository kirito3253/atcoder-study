import sys
import math

input_data = sys.stdin.read().strip().split()
n = int(input_data[0])
data = list(map(int, input_data[1:]))

average = math.ceil(sum(data) / n)
total = 0

for x in data:
    total += (x - average) ** 2

print(total)