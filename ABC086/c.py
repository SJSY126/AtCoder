n = int(input())
ans = 'Yes'
for i in range(n):
    t, x, y = map(int, input().split())
    if ans != "No":
        if x + y > t:
            ans = "No"
        else:
            if t % 2 == (x+y) % 2:
                ans = "Yes"
            else:
                ans = "No"
print(ans)
