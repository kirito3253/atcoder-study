def main():
    # 1. 入力を文字列として受け取る
    # 数値として計算する必要がないため、そのまま扱う
    s = input()
    
    # 2. 文字列の中に '1' がいくつあるかカウントする
    count = s.count('1')
    
    # 3. 結果を出力
    print(count)

if __name__ == "__main__":
    main()