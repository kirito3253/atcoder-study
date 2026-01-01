d, f = map(int, input().split())

temp = (d - f + 1) % 7
if temp == 0:
    answer = 1
else:
    answer = 7 - temp + 1

print(answer)