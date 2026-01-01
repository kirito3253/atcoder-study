import sys

def solve(a, b): # 文字列aを文字列bにするために必要な回数
    count = 0
    for j in range(len(a)):
        if int(a[j]) <= int(b[j]):
            count += int(b[j]) - int(a[j])
        else:
            count += int(b[j]) + 10 - int(a[j])
    return count
    
input_data = sys.stdin.read().split()

n = int(input_data[0])
m = int(input_data[1])
s = input_data[2]
t = input_data[3]
# tをsの部分文字列にする

count = 1000
for i in range(n-m+1):
    temp = solve(t, s[i:i+m])
    if temp < count:
        count = temp

print(count)