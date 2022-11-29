"""Tests for linked list utils."""

import pytest
from exercises.ex11.linked_list import Node, last, value_at, max, linkify, scale

__author__ = "Your PID"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_value_at_out_of_range() -> None:
    """Index integer is out of the range of the linked list's 'length'."""
    with pytest.raises(IndexError):
        linked_list = Node(1, Node(2, Node(3, None)))
        value_at(linked_list, 4)


def test_value_at_non_empty() -> None:
    """Return the middle value in a non-empty linked list."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert value_at(linked_list, 1) == 2


def test_max_empty() -> None:
    """Raises ValueError if linked list is empty."""
    with pytest.raises(ValueError):
        max(None)


def test_max_non_empty() -> None:
    """If the max function is not empty."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert max(linked_list) == 3
        
    
def test_linkify_empty() -> None:
    """The list of integers is empty."""
    items: list[int] = []
    assert linkify(items) is None

    
def test_linkify_empty_string() -> None:
    """The list is not of integers but strings."""
    items: list[str] = []
    assert linkify(items) is None

                  
def test_scale_empty() -> None:
    """The list is empty in the left side of the function."""
    assert (scale(linkify([]), 2)) is None


def test_scale_non_empty() -> None:
    """The list is empty in the left side of the function."""
    items: list[str] = []
    assert (scale(linkify(items), 2)) is None