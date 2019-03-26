s = list(input())
t = list(input())
n = len(s)

for i in range(n):
    if s[i] == "@":
        if t[i] in "atcoder@":
            s[i] = t[i]
    elif t[i] == "@":
        if s[i] in "atcoder@":
            t[i] = s[i]

if s == t:
    print('You can win')
else:
    print("You will lose")
