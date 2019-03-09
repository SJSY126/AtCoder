n = int(input())
i = 1
count = 0

while 1:
    print(i)
    if i > n:
        break
    s = set([])
    for j in str(i):
        if j == '0'  or j == '1' or j == '2' or j == '4' or j == '6' or j == '8' or j == '9':
            continue
        s.add(int(j))
    if s == set([3,5,7]):
        count = count + 1
    i = i + 2

print(count)
