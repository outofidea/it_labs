


for (idx, dig) in enumerate(map(int,reversed(list(input())))):
    if dig == 1: sum+= 2**idx

print(sum)