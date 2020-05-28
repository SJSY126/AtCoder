N, K = map(int, input().split())
d = [0 for _ in range(K)]
sunuke = [0 for _ in range(N)]

for i in range(K):
    d[i] = int(input())
    a = list(map(int, input().split()))
    for i in a:
        sunuke[i-1] += 1

print(sunuke.count(0))
