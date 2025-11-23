n, k = map(int, input().split())

ans = n
stem_cnt = n

while stem_cnt >= k:
    new_mushrooms = stem_cnt // k
    ans += new_mushrooms
    stem_cnt = stem_cnt % k + new_mushrooms

print(ans)