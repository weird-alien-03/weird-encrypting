# tests/test_prime_utils.py

from seed_utils import seed_from_text
from prime_utils import (
    bytes_to_candidate,
    is_probable_prime,
    next_prime_from_seed,
    derive_second_seed,
)


def test_bytes_to_candidate_is_odd_and_has_target_bits():
    seed = seed_from_text("hello")
    candidate = bytes_to_candidate(seed, 16)

    assert candidate % 2 == 1
    assert candidate.bit_length() == 16


def test_is_probable_prime_known_values():
    assert is_probable_prime(13) is True
    assert is_probable_prime(17) is True
    assert is_probable_prime(15) is False
    assert is_probable_prime(21) is False


def test_next_prime_from_seed_is_deterministic():
    seed = seed_from_text("hello")
    p1 = next_prime_from_seed(seed, 16)
    p2 = next_prime_from_seed(seed, 16)

    assert p1 == p2
    assert is_probable_prime(p1)


def test_derive_second_seed_changes_seed():
    seed = seed_from_text("hello")
    seed2 = derive_second_seed(seed)

    assert isinstance(seed2, bytes)
    assert seed2 != seed


def test_p_and_q_paths_can_differ():
    seed = seed_from_text("hello")
    seed2 = derive_second_seed(seed, b"q")

    p = next_prime_from_seed(seed, 16)
    q = next_prime_from_seed(seed2, 16)

    assert is_probable_prime(p)
    assert is_probable_prime(q)
