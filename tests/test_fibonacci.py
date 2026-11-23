import pytest

from sequence import fibonacci

def test_first_six_terms():
    assert fibonacci(6) == [0, 1, 1, 2, 3, 5]

@pytest.mark.parametrize(
    ("n", "expected"),
    [(0, []), (1, [0]), (2, [0, 1])],
)
def test_boundaries(n, expected):
    assert fibonacci(n) == expected

@pytest.mark.parametrize("n", [1.5, "3", True, None])
def test_non_integer_n_is_rejected(n):
    with pytest.raises(TypeError, match="integer"):
        fibonacci(n)

def test_negative_n_is_rejected():
    with pytest.raises(ValueError, match="non-negative"):
        fibonacci(-1)
