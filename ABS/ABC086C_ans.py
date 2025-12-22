import sys

def solve():
    # 入力の高速化
    input_data = sys.stdin.read().split()
    n = int(input_data[0])
    
    # 初期位置（t, x, y）
    prev_t, prev_x, prev_y = 0, 0, 0
    
    # データを順番に処理
    current_idx = 1
    for _ in range(n):
        t = int(input_data[current_idx])
        x = int(input_data[current_idx + 1])
        y = int(input_data[current_idx + 2])
        current_idx += 3
        
        # 移動時間と距離を計算
        dt = t - prev_t
        dist = abs(x - prev_x) + abs(y - prev_y)
        
        # 判定条件: 
        # 1. 距離が時間より長い場合は到達不可能
        # 2. (時間 - 距離) が奇数の場合は、その地点に止まれないため到達不可能
        if dist > dt or (dt - dist) % 2 != 0:
            print("No")
            return
        
        # 現在の地点を記録
        prev_t, prev_x, prev_y = t, x, y

    print("Yes")

if __name__ == "__main__":
    solve()