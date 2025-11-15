from __future__ import annotations

from .config import STAGES
from .puzzle import build_puzzle, check_answer
from flag import flag

BANNER = "\n##### Cerdas Cermath #####\n"

def run() -> None:
    print(BANNER)
    for stage in range(1, STAGES + 1):
        puzzle = build_puzzle()
        print(f"----- Stage [{stage}] -----\n")
        for i, pk in enumerate(puzzle.public_keys, 1):
            print(f"* n = {pk.n}")
            print(f"* e = {pk.e}")
        print(f"* c = {puzzle.ciphertext}\n")

        user_input = input("BPJS? Correct Answer Only ~> ").strip()
        if check_answer(user_input, puzzle.correct_answer):
            print("\nTrue!\n")
        else:
            print("False, Bye!")
            return

    print("Thank you for being so OP...")
    print(f"Congratulations! {flag}")
