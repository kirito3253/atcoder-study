def solve():
    n = int(input())
    # 1. カードを数値のリストとして受け取り、大きい順に並び替える
    cards = sorted(list(map(int, input().split())), reverse=True)
    
    # 2. スライシングを使って、AliceとBobのカードを抽出
    # Aliceは 0, 2, 4... 番目、Bobは 1, 3, 5... 番目
    alice_cards = cards[0::2]
    bob_cards = cards[1::2]
    
    # 3. それぞれの合計の差を出力
    print(sum(alice_cards) - sum(bob_cards))

if __name__ == "__main__":
    solve()