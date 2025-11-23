sum = 0
for (idx, dig) in enumerate(reversed(list(input()))):
    if dig == "1": sum+= 2**idx
print(sum)