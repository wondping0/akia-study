<div align="center">

# akia-study

**Study scratchpad: a small RSA quiz challenge, a base-conversion reversal script and symmetric-cipher helpers.**

![Python](https://img.shields.io/badge/Python-3-38E1FF?style=flat-square&labelColor=0A1428&logo=python&logoColor=38E1FF)
![pycryptodome](https://img.shields.io/badge/pycryptodome-required-38E1FF?style=flat-square&labelColor=0A1428)

</div>

---

## Overview

This is a working repo of practice material rather than one finished project. It contains three unrelated pieces.

### Cerdas Cermat (RSA quiz challenge)

A CTF-style quiz service (*"Cerdas Cermath"*). It has 100 stages (`STAGES`), and each stage:

- generates 3 RSA key pairs with 1024-bit moduli (`KEYS_PER_STAGE`, `BITS`);
- picks one of five fixed phrases from `config.ANSWERS`, all with the initials B.P.J.S. (e.g. *"Be Positive, Just Smile"*);
- encrypts the phrase with textbook RSA under one of the three public keys, chosen at random;
- prints all three `(n, e)` pairs and the ciphertext, then asks for the exact phrase.

Answering every stage correctly prints the flag.
Note the key generation in `crypto_utils.py`: the private exponent `d` is drawn from `[max_d/2, max_d)` with `max_d = isqrt(isqrt(2^1024)) // 3`, i.e. below `N^(1/4) / 3`.
No solver for this challenge is included.

`dist.zip` is the handout archive; its `src/` is identical to `Cerdas Cermat/src/`.

### solve.py

This script reverses a transformation shown in its header comment. A secret is turned into an integer, then for each base `b = 10..24` it is rewritten as `int(str(x), b)` (its decimal digits read in base `b`).
`reverse_step` undoes one step by writing the number in base `b` and reading those digits back as decimal. `reverse_all` applies this for `b = 24` down to `10` and converts the result to bytes.

### simetris.py and test.py

Small pycryptodome helpers:

- `simetris.py`: AES-ECB encrypt/decrypt and 3DES-ECB encrypt (with PKCS#7 padding).
- `test.py`: AES-ECB round trip on a sample message with a 16-byte demo key.

## Files

| Path | Description |
| --- | --- |
| `Cerdas Cermat/src/app.py` | Entry point, calls `modules.cli.run()` |
| `Cerdas Cermat/src/modules/cli.py` | Stage loop, I/O, answer check, prints the flag |
| `Cerdas Cermat/src/modules/config.py` | `BITS`, `STAGES`, `KEYS_PER_STAGE`, `ANSWERS` |
| `Cerdas Cermat/src/modules/crypto_utils.py` | RSA key generation (small `d`) and textbook encryption |
| `Cerdas Cermat/src/modules/puzzle.py` | Builds one stage and checks the answer |
| `Cerdas Cermat/src/modules/models.py` | `PublicKey`, `RSASecret`, `Puzzle` dataclasses |
| `Cerdas Cermat/dist.zip` | Handout archive of `src/` |
| `solve.py` | Reverses the repeated base-conversion transform |
| `simetris.py` | AES-ECB / 3DES-ECB helpers |
| `test.py` | AES-ECB round-trip demo |

## Requirements

- Python 3
- [`pycryptodome`](https://pypi.org/project/pycryptodome/)

```bash
pip install pycryptodome
```

## Usage

```bash
python solve.py
python test.py
```

Run the quiz locally. It imports `flag` from a `flag.py` module that isn't in the repo, so create one first:

```bash
cd "Cerdas Cermat/src"
echo 'flag = "flag{test}"' > flag.py
python app.py
```

---

<div align="center">

Part of [wondping0](https://github.com/wondping0)'s cryptography notebooks · [wondping0.github.io](https://wondping0.github.io)

</div>
