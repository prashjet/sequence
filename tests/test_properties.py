from hypothesis import given, strategies as st

from sequence import fibonacci

@given(st.integers(min_value=2, max_value=100))
def test_fibonacci_recurrence(n):
    seq = fibonacci(n + 1)
    assert seq[n] == seq[n - 1] + seq[n - 2]