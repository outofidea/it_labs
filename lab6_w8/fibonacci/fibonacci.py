num = int(input())

arr = [0, 1]

if num <= 2:
    print(arr[num - 1])
else:
    for lol in range(0, num - 1):
        if lol % 2 == 1:
            arr[1] += arr[0]
            choice = 1
        if lol % 2 == 0:
            arr[0] += arr[1]
            choice = 0
    print(arr[choice])
