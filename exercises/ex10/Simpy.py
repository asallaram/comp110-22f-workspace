"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730557183"


class Simpy:
    """Data Analysis object."""
    values: list[float]

    def __init__(self, values: list[float]):
        """Constructor class for Simpy."""
        self.values = values

    def __repr__(self) -> str:
        """When Simpy object is converted to str representation."""
        return f"Simpy({self.values})"

    def fill(self, fill: float, num: int) -> None:
        """Fill a Simpy's values with specific number of repeating values."""
        i: int = 0
        self.values = ([])
        while i < num:
            self.values.append(fill)
            i += 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill in the values attribute with range of values in terms of floats."""
        assert step != 0.0
        self.values = ([])
        while abs(start) < abs(stop):
            self.values.append(start)
            start += step

    def sum(self) -> float:  
        """Add up all the values in Simpy."""          
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Add two Simpy objects together."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for value in self.values:
                value += rhs
                result.values.append(value)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.values.append(self.values[i] + rhs.values[i])
        return result

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Raise a Simpy method to a certain power or another Simpy."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for value in self.values:
                value **= rhs
                result.values.append(value)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.values.append(self.values[i] ** rhs.values[i])
        return result
    
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Sets Simpy equal to a float value or another Simpy and returns mask values."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for value in self.values:
                if value == rhs:
                    result.append(True)
                else:
                    result.append(False)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                if self.values[i] == rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Sets Simply greater than to a float value or another Simpy and returns mask values."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for value in self.values:
                if value > rhs:
                    result.append(True)
                else:
                    result.append(False)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                if self.values[i] > rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Either returns the certain indice of a Simpy or returns True values of a Simpy that is masked."""
        result: Simpy = Simpy([])
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            for i in range(len(self.values)):
                if rhs[i] is True:
                    result.values.append(self.values[i])
        return result