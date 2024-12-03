import sympy
from sympy.core.intfunc import mod_inverse
from sympy.ntheory.generate import randprime


def gen_prime(e, a, b):
    while True:
        p = randprime(a, b)

        if sympy.gcd(e, p) == 1:
            return p


def gen_primes(e, a, b, n):
    while True:
        p1 = gen_prime(e, a, b)
        p2 = gen_prime(e, a, b)
        M = p1 * p2

        if len(str(M)) == n:
            return p1, p2


E = 65537
A = 10**91
B = 10**93
N = 186

p1, p2 = gen_primes(E, A, B, N)
M = p1 * p2
phi_M = (p1 - 1) * (p2 - 1)
D = mod_inverse(E, phi_M)

print(f"isprime(p1) = {sympy.isprime(p1)}")
print(f"isprime(p2) = {sympy.isprime(p2)}")
print(f"len(M) = {len(str(M))}")
print(f"gcd(D, phi_M) = {sympy.gcd(D, phi_M)}")

with open("key_A.txt", "w", encoding="utf8") as file:
    file.write(f"{E}\n")
    file.write(f"{p1}\n")
    file.write(f"{p2}\n")
    file.write(f"{M}\n")
    file.write(f"{D}\n")
