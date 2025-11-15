from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class PublicKey:
    n: int
    e: int

@dataclass(frozen=True)
class RSASecret:
    n: int
    e: int
    d: int
    phi: int

@dataclass(frozen=True)
class Puzzle:
    public_keys: list[PublicKey]
    ciphertext: int
    correct_answer: bytes
