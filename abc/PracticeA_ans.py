# 改善後のコード
def main():
    # 1. 数値の入力を受け取る
    num_a = int(input())
    
    # 2. スペース区切りの数値を受け取り、合計を計算する
    # mapオブジェクトをアンパックして合計を求める
    num_b, num_c = map(int, input().split())
    
    # 3. 文字列を受け取る
    text_s = input()

    # 4. 合計値と文字列をフォーマットして出力
    total_value = num_a + num_b + num_c
    print(f"{total_value} {text_s}")

if __name__ == "__main__":
    main()