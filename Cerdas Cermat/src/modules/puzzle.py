from __future__ import annotations

import secrets
from .config import KEYS_PER_STAGE, ANSWERS
from .crypto_utils import generate_keypair, encrypt
from .models import PublicKey, Puzzle

def build_puzzle(rng: secrets.SystemRandom | None = None) -> Puzzle:
    rng = rng or secrets.SystemRandom()
    secrets_list = [generate_keypair() for _ in range(KEYS_PER_STAGE)]
    public_keys = [PublicKey(n=s.n, e=s.e) for s in secrets_list]
    answer = rng.choice(ANSWERS)
    answer_bytes = answer.encode()
    chosen_pub = rng.choice(public_keys)
    c = encrypt(answer_bytes, chosen_pub.n, chosen_pub.e)
    rng.shuffle(public_keys)
    return Puzzle(public_keys=public_keys, ciphertext=c, correct_answer=answer_bytes)

def check_answer(user_input: str, correct_answer: bytes) -> bool:
    try:
        return user_input.encode() == correct_answer
    except (UnicodeEncodeError, ValueError):
        return False