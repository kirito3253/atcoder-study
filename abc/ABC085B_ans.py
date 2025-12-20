# 入力回数 N を取得
n = int(input())

# 全ての入力をセット（集合）に格納して重複を自動排除
mochi_set = {int(input()) for _ in range(n)}

# 重複を除いた要素の数を出力
print(len(mochi_set))