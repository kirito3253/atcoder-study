# 4文字以上がアンバランスな場合は、どこかにアンバランスな2文字、3文字が必ず存在する
def solve():
    s = input()
    n = len(s)

    # 隣り合う2文字をチェック (例: "aa")
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            print(i + 1, i + 2)
            return

    # 1文字飛ばしの3文字をチェック (例: "aba")
    for i in range(n - 2):
        if s[i] == s[i + 2]:
            print(i + 1, i + 3)
            return

    # 見つからなかった場合
    print(-1, -1)

solve()