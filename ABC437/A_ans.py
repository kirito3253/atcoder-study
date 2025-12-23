import sys

def solve():
    # 標準入力から1行読み込み、空白で分割して整数に変換
    # sys.stdin.readline は input() より高速です
    x, y = map(int, sys.stdin.readline().split())
    
    # 1フィート = 12インチなので、計算して出力
    print(x * 12 + y)

if __name__ == '__main__':
    solve()