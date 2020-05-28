n = int(input())
a = list(map(int, input().split()))
dic = {}
for i in a:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
ans = 0
for k, v in dic.items():
    if k > v:
        ans += v
    elif k < v:
        ans += v-k

print(ans)
