# 改善案：ソートを利用した直感的な比較
def main():
    # 入力を取得（list()によるキャストは split() の時点でリストなので不要）
    data = input().split()

    # ソートして期待されるパターン ['5', '5', '7'] と一致するか確認
    if sorted(data) == ['5', '5', '7']:
        print('YES')
    else:
        print('NO')

if __name__ == "__main__":
    main()