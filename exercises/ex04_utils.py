"""This program will use lists and functions for the purpose of comparision."""


__author__ = "730557183"


def all(numbers: list[int], search: int) -> bool:
    """This function will search a list of integers for a certain integer value and return a boolean based on that."""
    i: int = 0
    track: bool = True
    if numbers == []:
        return False
    while i < len(numbers) and track:
        if numbers[i] == search:
            track = True
            i += 1
        else:
            track = False
    return track      


def max(largest: list[int]) -> int:
    """This function will search for the max number  in a list."""
    if len(largest) == 0:
        raise ValueError("max() arg is an empty List")
    r: int = 0
    highest: int = -10
    while r < len(largest):
        if largest[r] > highest:
            highest = largest[r]
            r += 1
        else:
            r += 1
    return highest


def is_equal(equal_a: list[int], equal_b: list[int]) -> bool:
    """This function will compare two lists and determine if every element at every index is equal."""
    j: int = 0
    d: int = 0
    watch: bool = True
    if len(equal_a) != len(equal_b):
        return False
    while j < len(equal_a) and d < len(equal_b) and watch:
        if equal_a[j] == equal_b[j]:
            watch = True
            j += 1
            d += 1
        else:
            watch = False
    if watch:
        return True
    else:
        return False