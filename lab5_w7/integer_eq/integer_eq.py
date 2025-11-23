a, b = map(int, input().split())

if a == 0:
    if b == 0:
        print("INFINITE SOLUTIONS")
    else:
        print("NO SOLUTION")
else:
    if b % a != 0:
        print("NO SOLUTION")
    else:
        print(-b // a)
