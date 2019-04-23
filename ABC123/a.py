antenna = [0]*5
for i in range(5):
    antenna[i] = int(input())

k = int(input())
ans = "Yay!"

for i in range(5):
    if antenna[0] + k < antenna[i]:
        ans = ":("
        break

print(ans)
