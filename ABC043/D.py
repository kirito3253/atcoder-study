def check(s):
    for i in range(2, len(s) + 1):
        idx = 0
        for _ in range(len(s) - i + 1):
            text = s[idx:idx + i]
            for x in text:
                if text.count(x) > len(text) // 2:
                    return idx + 1, idx + i
            idx += 1
    return -1, -1

s = list(input())
a, b = check(s)
print(a, b)