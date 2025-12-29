import sys
import itertools

input_data = sys.stdin.read().split()

n = int(input_data[0])
a = int(input_data[1])
data = input_data[2:]

count = 0
for i in range(1, n+1):
    for j in itertools.combinations(data, i):
        j = list(map(int, j))
        if sum(j) / i == a:
            count += 1

print(count)