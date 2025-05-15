# Write a python program for RSA system, the public key of a given user is e = 31, n = 3599
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

e = 31
n = 3599

for p in range(2, int(n**0.5) + 1):
    if n % p == 0:
        q = n // p
        break

f_n = (p - 1) * (q - 1)
gcd, d, _ = extended_gcd(e, f_n)
d = d % f_n
if d < 0:
    d += f_n

print(f"Private key: {d}")