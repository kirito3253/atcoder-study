def main():
    # 1. 入力を受け取る
    num_a, num_b = map(int, input().split())
    
    # 2. 偶奇の判定
    # 積が偶数になるのは「少なくとも一方が偶数」の時
    if (num_a * num_b) % 2 == 0:
        print("Even")
    else:
        print("Odd")

if __name__ == "__main__":
    main()