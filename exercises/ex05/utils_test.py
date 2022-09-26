"""Where the edge cases and use cases will be located."""


__author__ = "730557183"


from utils import only_evens, concat, sub


def test_only_evens_empty() -> None:
    """The only_evens list is empty."""
    assert only_evens([]) == []


def test_only_evens_many() -> None:
    """There are many numbers in only_evens."""
    assert only_evens([2, 3, 5, 6, 8]) == [2, 6, 8]


def test_only_evens_negative() -> None:
    """The numbers in only_evens are all negative."""
    assert only_evens([-2, -4, -5, -6, -8]) == [-2, -4, -6, -8]


def test_concat_empty() -> None:
    """Concat list is empty."""
    assert concat([], []) == []


def test_concat_xf_empty() -> None:
    """The first list in concat is empty."""
    assert concat([], [2, 3, 4]) == [2, 3, 4]


def test_concat_xr_empty() -> None:
    """The second list in concat is empty."""
    assert concat([2, 3, 4], []) == [2, 3, 4]


def test_sub_start_negative() -> None:
    """The start index is negative."""
    assert sub([1, 2, 3], -5, 3) == [1, 2, 3]


def test_sub_end_greater() -> None:
    """The end index is greater than the length of the list."""
    assert sub([1, 2, 3], 0, 5) == [1, 2, 3]


def test_sub_empty() -> None:
    """The sub list is empty."""
    assert sub([], 5, 8) == []


def test_sub_start_greater() -> None:
    """The start index is greater than the length of the list."""
    assert sub([2, 3, 4], 5, 8) == []


def test_sub_end_atmost_0() -> None:
    """The end index of the list is 0."""
    assert sub([2, 3, 4], 5, 0) == []