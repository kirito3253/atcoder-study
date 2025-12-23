import sys

def solve():
    # 全入力を一括で読み込み、空白・改行で分割
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    h = int(input_data[0])
    w = int(input_data[1])
    n = int(input_data[2])
    
    # グリッドの読み込み (h行w列)
    # data[i] に i行目のリストが入る
    idx = 3
    grid = []
    for _ in range(h):
        grid.append(input_data[idx : idx + w])
        idx += w
        
    # 呼ばれた数字を集合型 (set) に変換
    # 検索にかかる時間が O(N) から O(1) になります
    called_numbers = set(input_data[idx : idx + n])
    
    max_count = 0
    for row in grid:
        # この行に含まれる数字のうち、called_numbersにあるものの個数を数える
        current_row_count = 0
        for num in row:
            if num in called_numbers:
                current_row_count += 1
        
        # 最大値を更新
        if current_row_count > max_count:
            max_count = current_row_count
            
    print(max_count)

if __name__ == '__main__':
    solve()