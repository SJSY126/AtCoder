n = int(input())
a = list(map(int, input().split()))

ave = sum(a)/(n-a.count(0))
if ave % 1 != 0:
    ans = ave//1 + 1
else:
    ans = ave//1
print(int(ans))
