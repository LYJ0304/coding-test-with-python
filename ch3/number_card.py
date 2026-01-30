n, m = map(int, input().split()) # n은 행, m은 열
card = []
for i in range(n):
    card_list = list(map(int, input().split()))
    card.append(card_list)

result = []
for k in card:
    result.append(min(k))

print(max(result))
