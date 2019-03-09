w = list(input())

for i in w:
    if i not in {"a", "i", "u", "e", "o"}:
        print(i, end="")
print()
