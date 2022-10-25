"""Dictionary related utility functions."""

__author__ = "730557183"

# Define your functions below

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []

    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)
    
    # Read that File

    # Close the file when we're done, to free its resources.
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(dict1: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Produce a column-based table with only first N(a parameter) rows of data for each column."""
    dict2: dict[str, list[str]] = {}
    for column in dict1:
        result: list[str] = []
        i: int = 0
        if rows >= len(dict1[column]):
            rows = len(dict1[column])
        while i < rows:
            result.append(dict1[column][i])
            i += 1
        dict2[column] = result
    return dict2


def select(dict1: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Produce column-based table with only a specific subset of original columns."""
    dict2: dict[str, list[str]] = {}
    for column in names:
        dict2[column] = dict1[column]
    return dict2


def concat(dict1: dict[str, list[str]], dict2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce column-based table with two column-based tables combined."""
    dict3: dict[str, list[str]] = {}
    for column in dict1:
        dict3[column] = dict1[column]
    for column in dict2:
        if column in dict3:
            dict3[column] += dict2[column]
        else:
            dict3[column] = dict2[column]
    return dict3


def count(list1: list[str]) -> dict[str, int]:
    """Produce a dictionary where each key is a unique value in the given list and each value associated is count of number of times that value appeared in the input list."""
    dict1: dict[str, int] = {}
    for value in list1:
        if value in dict1:
            dict1[value] += 1
        else:
            dict1[value] = 1
    return dict1