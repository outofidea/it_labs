n = int(input())
count = 0

for x1 in range(1, n + 1):
    for x2 in range(x1 + 1, n + 1):
        for x3 in range(x2 + 1, n + 1):
            x4 = n - x1 - x2 - x3
            if x4 > x3:
                count += 1

print(count)