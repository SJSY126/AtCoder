n = int(input())
card = [1, 2, 3, 4, 5, 6]
n = n % 30
for i in range(n):
    a = (i % 5)
    b = a + 1
    card[a], card[b] = card[b], card[a]

print("".join(map(str, card)))
