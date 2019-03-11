def two(l, r):
    ret = [i*((-1)**i) for i in range(l, r+1)]
    ans=0
    for item in ret:
        ans += item
    return ans
print(two(2, 4))