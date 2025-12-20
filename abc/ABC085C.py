def check(n, y):
    for i in range(0, n+1):
        for j in range(0, n-i+1):
            k = n-i-j
            if 10000*i + 5000*j + 1000*k == y:
                return i, j, k
                
    return -1, -1, -1

n, y = map(int, input().split())
i, j, k = check(n, y)
print(i, j, k)