n = int(input())
if n <= 1:
    print("NO")
else:
    result = "YES"  
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            result = "NO"
            break
    print(result)