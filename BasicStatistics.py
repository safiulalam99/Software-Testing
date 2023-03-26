import statistics
from typing import List, Union, Tuple


class BasicStatistics:
    """
    A class that provides basic statistics calculations.
    """

    @staticmethod
    def mean(numbers: List[float]) -> float:
        """
        Calculate the mean of a list of numbers.

        Args:
            numbers (List[float]): A list of numbers.

        Returns:
            float: The mean of the list of numbers.
        """
        if not numbers:
            raise ValueError("List cannot be empty")
        return sum(numbers) / len(numbers)

    @staticmethod
    def median(numbers: List[float]) -> float:
        """
        Calculate the median of a list of numbers.

        Args:
            numbers (List[float]): A list of numbers.

        Returns:
            float: The median of the list of numbers.
        """
        numbers.sort()
        n = len(numbers)
        if n % 2 == 0:
            return (numbers[n // 2 - 1] + numbers[n // 2]) / 2
        else:
            return numbers[n // 2]

    @staticmethod
    def mode(numbers: List[float]) -> List[float]:
        """
        Calculate the mode of a list of numbers.

        Args:
            numbers (List[float]): A list of numbers.

        Returns:
            List[float]: A list of the mode(s) of the list of numbers.
        """
        return list(statistics.multimode(numbers))

    @staticmethod
    def range_of_numbers(numbers: List[float]) -> float:
        """
        Calculate the range of a list of numbers.

        Args:
            numbers (List[float]): A list of numbers.

        Returns:
            float: The range of the list of numbers.
        """
        return max(numbers) - min(numbers)

    @staticmethod
    def standard_deviation(numbers: List[float]) -> float:
        """
        Calculate the standard deviation of a list of numbers.

        Args:
            numbers (List[float]): A list of numbers.

        Returns:
            float: The standard deviation of the list of numbers.
        """
        return statistics.stdev(numbers)
