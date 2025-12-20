n = int(input())
mochi = []

for i in range(n):
    mochi.append(int(input()))

mochi.sort(reverse=True)

# 最初の一個は必ずおける
total = 1

for i in range(1, n):
    if mochi[i] != mochi[i-1]:
        total += 1

print(total)
