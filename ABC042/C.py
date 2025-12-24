import sys

input_data = sys.stdin.read().split()
n = input_data[0]
k = int(input_data[1])
unlike_nums = set(input_data[2:])

answer = []
for i in n:
    temp = i
    while temp in unlike_nums:
        temp = str(int(temp) + 1)
    answer.append(temp)

print("".join(answer))