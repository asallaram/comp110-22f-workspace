"""User and edge cases for any funcions written in dictionary."""

__author__ = "730557183"

from dictionary import invert, favorite_color, count


def test_invert_empty() -> None:
    """The dictionary for invert is empty."""
    assert invert({}) == {}


def test_invert_is_many() -> None:
    """The dictionary for invert is made up of many values."""
    assert invert({"Giants": "1", "Packers": "2", "Patriots": "3", "Eagles": "4"}) == {"1": "Giants", "2": "Packers", "3": "Patriots", "4": "Eagles"}


def test_invert_is_similar() -> None:
    """The dictionary for invert is made up of similar but not same values."""
    assert invert({"Giants": "Win", "Packers": "Won"}) == {"Win": "Giants", "Won": "Packers"}


def test_favorite_color_empty() -> None:
    """The dictionary for favorite_color is empty."""
    assert favorite_color({}) == ("") 


def test_favorite_color_is_many() -> None:
    """The dictionary for favorite_color is made up of many values."""
    assert favorite_color({"Aneesh": "Giants", "Sam": "Giants", "Carter": "Brown", "Eshaan": "Eagles"}) == ("Giants")


def test_favorite_color_is_same_keys() -> None:
    """The dictionary for favorite colors is made up of same keys and values."""
    assert favorite_color({"Giants": "Giants", "Packers": "Packers", "Eagles": "Giants"}) == ("Giants")


def test_count_is_empty() -> None:
    """The list for count is empty."""
    assert count([]) == {}


def test_count_is_many() -> None:
    """The list for invert is made up of many strings."""
    assert count(["Cheese", "Cheese", "Packers", "Giants Win Again", "Big Blue"]) == {"Cheese": 2, "Packers": 1, "Giants Win Again": 1, "Big Blue": 1}


def test_count_is_integers_as_strings() -> None:
    """The list for invert is made up of integers as strings."""
    assert count(["1", "1", "2", "2"]) == {"1": 2, "2": 2}