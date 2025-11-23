n = int(input())

result = ''  # binary result

while n > 0:
    result += str(n % 2)
    n //= 2
    
print(result[::-1])