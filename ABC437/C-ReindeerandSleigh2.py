t = int(input())
cases = []
for _ in range(t):
    n = int(input())
    case = []
    for _ in range(n):
        data = list(map(int, input()))
        case.append(data)
    cases.append(case)

print(case)
        