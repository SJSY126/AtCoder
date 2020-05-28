K = int(input())
S = input()

if len(S) < K + 1:
    print(S)

else:
    print(S[:K]+'...')
