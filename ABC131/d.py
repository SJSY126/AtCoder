n = int(input())
jobs = []

for i in range(n):
    ai, bi = map(int, input().split())
    jobs.append([ai, bi])

jobs = sorted(jobs, key=lambda x: x[1])

ans = "Yes"
limit = 0
time = 0
for job in jobs:
    time += job[0]
    limit = job[1]
    if limit < time:
        ans = "No"
        break

print(ans)
