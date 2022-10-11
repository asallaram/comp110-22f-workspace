"""Functions will be defined here for anything related to the dictionary."""

__author__ = "730557183"


def invert(dict1: dict[str, str]) -> dict[str, str]:
    """This function will invert the keys and values of a dictionary."""
    dict2: dict[str, str] = {}
    for item in dict1:
        if dict1[item] in dict2:
            raise KeyError("You cannot have same values for this function!")
        dict2[dict1[item]] = item
    return (dict2)


def favorite_color(dict1: dict[str, str]) -> str:
    """This function will return the color that appears most frequently or if tied, the first color."""
    dict2: dict[str, int] = {}
    for item in dict1:
        if dict1[item] in dict2:
            dict2[dict1[item]] += 1
        else:
            dict2[dict1[item]] = 1
    high: str = ""
    highest: int = 0
    for item in dict2:
        current_high = dict2[item]
        if current_high > highest:
            highest = current_high
            high = item
    return high


def count(list1: list[str]) -> dict[str, int]:
    """This function will count the number of times a certain item appears in a list and then assign name and value in a dictionary."""
    dict1: dict[str, int] = {}
    for item in list1:
        if item in dict1:
            dict1[item] += 1
        else:
            dict1[item] = 1
    return dict1