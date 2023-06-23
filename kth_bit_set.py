def is_kth_bit_set(n, k):
    if n & (1 << (k - 1)):
        return "SET"
    else:
        return "NOT SET"

n = 5
k = 1
result = is_kth_bit_set(n, k)
print(result)
