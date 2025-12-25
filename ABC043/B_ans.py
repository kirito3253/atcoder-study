def solve():
    s = input()
    ans = []

    for char in s:
        if char == '0' or char == '1':
            ans.append(char)
        elif char == 'B' and ans:
            ans.pop()

    print("".join(ans))

if __name__ == '__main__':
    solve()