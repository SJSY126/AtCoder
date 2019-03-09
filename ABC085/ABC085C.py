n , sum = map(int, input().split())

sum = int(sum / 1000)

if sum < n or 10 * n < sum:
    print(-1, -1, -1)

elif sum == n:
    print(0, 0, n)

elif sum == 10 * n:
    print(n, 0, 0)

elif sum == 5 * n:
    print(0, n, 0)

else:
    output_x, output_z, output_y = -1, -1, -1
    n_min = int(sum/10)
    for i in range(n_min, n):
        max_y = int((9 * n - 10 * i + sum) / 4)
        for y in range(max_y):
            x = 10 * n - sum - 5 * y
            if x >= 0 and x % 9 == 0:
                x = int(x // 9)
                y = y
                z = n - (x + y)
                if z < 0:
                    break
                elif x >= 0 and y >= 0 and z >= 0:
                    output_z, output_y, output_x = z, y , x
                    break
        if output_x >= 0:
            break

    print(output_z, output_y, output_x)
