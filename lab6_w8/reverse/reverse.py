num1, num2 = map(int, input().split())
print(str(num1 + num2)[::-1].lstrip("0"))
