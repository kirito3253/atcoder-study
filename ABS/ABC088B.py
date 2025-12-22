n = int(input())
card = list(map(int, input().split()))

alice, bob = 0, 0

while sum(card) != 0:
    alice += max(card)
    card[card.index(max(card))] = 0
    
    bob += max(card)
    card[card.index(max(card))] = 0

print(alice - bob)