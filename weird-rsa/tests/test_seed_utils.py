# tests/test_seed_utils.py

from seed_utils import seed_from_text, seed_from_file, seed_from_system


def test_seed_from_text_is_reproducible():
    s1 = seed_from_text("hello quantum")
    s2 = seed_from_text("hello quantum")

    assert isinstance(s1, bytes)
    assert isinstance(s2, bytes)
    assert s1 == s2
    assert len(s1) == 32


def test_seed_from_file_is_reproducible(tmp_path):
    f = tmp_path / "sample.txt"
    f.write_text("weird encrypting project")

    s1 = seed_from_file(str(f))
    s2 = seed_from_file(str(f))

    assert isinstance(s1, bytes)
    assert isinstance(s2, bytes)
    assert s1 == s2
    assert len(s1) == 32


def test_seed_from_system_returns_bytes_of_requested_length():
    s = seed_from_system(32)

    assert isinstance(s, bytes)
    assert len(s) == 32
