import sys

def main():
    # 標準入力からすべての単語をリストとして取得
    # input_data[0] = n, input_data[1] = l
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # 実際の文字列データのみを取得してソート
    # スライス input_data[2:] で 3番目以降の要素をすべて指定
    words = input_data[2:]
    words.sort()

    # 高速な連結手法を用いて出力('+'だと非効率)
    result = "".join(words)
    print(result)

if __name__ == "__main__":
    main()