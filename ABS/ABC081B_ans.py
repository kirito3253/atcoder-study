# 改善版コード
def main():
    # 入力を受け取る
    n = int(input())
    data = list(map(int, input().split()))
    count = 0

    # 全ての要素が偶数である間、処理を繰り返す
    while all(x % 2 == 0 for x in data):
        # リスト内包表記で各要素を2で割る
        data = [x // 2 for x in data]
        count += 1

    print(count)

if __name__ == "__main__":
    main()