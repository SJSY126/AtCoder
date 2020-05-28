s = list(input())
ans = 'Yes'

if len(set(s)) != 2:
    ans = 'No'

if s.count(s[0]) != 2 or s.count(s[1]) != 2 or s.count(s[2]) != 2:
    ans = 'No'

print(ans)
