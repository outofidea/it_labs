(a,b,c,d) = tuple(map(int, input().split()))

if a == c or a == d or b == c or b == d:
    print("YES")
else:
    print("NO")