n = int(input())
words = [input() for _ in range(n)]

answered = set([words[0]])
ans = "Yes"

for i in range(1, n):
    if words[i] in answered:
        ans = "No"
        break

    if words[i][0] != words[i-1][-1]:
        ans = "No"
        break

    answered.update([words[i]])

print(ans)
