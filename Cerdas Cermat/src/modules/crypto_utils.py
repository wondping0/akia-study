from __future__ import annotations

import secrets
from math import isqrt, gcd
from Crypto.Util.number import getPrime, bytes_to_long
from .config import BITS
from .models import RSASecret

def generate_keypair(bits: int = BITS, rng: secrets.SystemRandom | None = None) -> RSASecret:
    rng = rng or secrets.SystemRandom()
    max_d = isqrt(isqrt(1 << bits)) // 3
    half_bits = bits // 2
    d_min = max_d // 2

    while True:
        p = getPrime(half_bits)
        q = getPrime(half_bits)
        if p == q:
            continue

        n = p * q
        phi = (p - 1) * (q - 1)

        for _ in range(10_000):
            span = max(1, max_d - d_min)
            d = d_min + rng.randrange(span)

            if gcd(d, phi) != 1:
                continue

            try:
                e = pow(d, -1, phi)
            except ValueError:
                continue

            if e.bit_length() > half_bits:
                return RSASecret(n=n, e=e, d=d, phi=phi)

def encrypt(message: bytes, n: int, e: int) -> int:
    m = bytes_to_long(message)
    if m >= n:
        raise ValueError("Too large!")
    return pow(m, e, n)
