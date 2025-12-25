import sys

input_data = sys.stdin.read().split()
n = int(input_data[0])
data = list(map(int, input_data[1:]))

ans = float('inf')

# -100から100まで全ての整数をターゲットとして試す
for target in range(-100, 101):
    current_cost = 0
    for x in data:
        current_cost += (x - target) ** 2
    
    if current_cost < ans:
        ans = current_cost

print(ans)