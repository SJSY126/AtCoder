a, b = map(int, input().split())

s = list(input())

ans = 'Yes'
for i in range(len(s)):
    if i == a:
        if s[i] != '-':
            ans = "No"
            break
    else:
        if s[i] not in "0123456789":
            ans = "No"
            break

print(ans)
