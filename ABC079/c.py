s = str(input())
ans = 0
for i in range(1 << (len(s)-1)):
    si = s[0]
    for j in range(len(s)-1):
        if i & (1 << j):
            si += "+"+s[j+1]
        else:
            si += "-"+s[j+1]
    if eval(si) == 7:
        break

print(si+"=7")
