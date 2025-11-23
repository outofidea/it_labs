lol = int(input())

remaining_min = lol % 3600

remaining_sec = remaining_min % 60

hours = (lol - remaining_min) / 3600

minutes = (remaining_min - remaining_sec) / 60

print(f"{int(hours)} {int(minutes)} {int(remaining_sec)}")
