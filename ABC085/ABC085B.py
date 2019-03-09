n = int(input())

mochis = []

for i in range(n):
    mochis.append(int(input())) 

kagami_mochis = set(mochis)
print(len(kagami_mochis))
