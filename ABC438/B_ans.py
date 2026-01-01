# 入力の受け取り
n, m = map(int, input().split())
s = input()
t = input()

# 最小値を保持する変数（非常に大きい値で初期化しておく）
min_operations = float('inf')

# S の中のどこから T を開始するかを全探索する
# i は S における T の開始位置（0 から N-M まで）
for i in range(n - m + 1):
    current_operations = 0
    
    # T の各文字について、S[i+j] に書き換えるためのコストを計算
    for j in range(m):
        target = int(s[i + j])  # 目標とする S の文字
        current = int(t[j])     # 現在の T の文字
        
        # current から target に変えるための操作回数
        # (例: 9 から 0 にするには (0 - 9 + 10) % 10 = 1 回)
        diff = (target - current + 10) % 10
        current_operations += diff
        
    # これまでの最小値と比較して更新
    if current_operations < min_operations:
        min_operations = current_operations

print(min_operations)