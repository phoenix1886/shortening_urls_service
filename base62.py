from string import ascii_lowercase, ascii_uppercase, digits
from math import floor

def base10_to_base62(num):
    base = digits + ascii_lowercase + ascii_uppercase
    r = num % len(base)
    res = base[r]
    q = floor(num / len(base))
    while q:
        r = q % len(base)
        q = floor(q / len(base))
        res = base[int(r)] + res
    return res


def base62_to_base10(num):
    base = digits + ascii_lowercase + ascii_uppercase
    limit = len(num)
    res = 0
    for i in range(limit):
        res = 62 * res + base.find(num[i])
    return res
