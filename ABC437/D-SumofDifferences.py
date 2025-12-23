import itertools

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

total = 0

total = sum(abs(i-j) for i, j in itertools.product(a,b))

print(total%998244353)