"""Unit Tests using lists and certain types of lists."""


__author__ = "730557183"


def only_evens(xs: list) -> list[int]:
    """This function will look for the even numbers in a test and then return the evens in a new list."""
    evens_list = []
    for item in xs:
        if item % 2 == 0:
            evens_list.append(item)
    return evens_list 


def concat(xf: list, xr: list) -> list[int]:
    """Concatenates two lists together and makes a bigger list."""
    concat_list = []
    for item in xf:
        concat_list.append(item)
    for item in xr:
        concat_list.append(item)
    return concat_list


def sub(xq: list, start: int, end: int) -> list[int]:
    """Given a list of integers, return a list of the numbers between two indexes with end being not inclusive."""
    sub_list = []
    for item in xq[start: end]:
        sub_list.append(item)
    return sub_list