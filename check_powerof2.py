def is_pow2(n):
    if n == 0:
        return True
    return (n & (n - 1)) == 0

n = 4
print(str(is_pow2(n)).lower())
