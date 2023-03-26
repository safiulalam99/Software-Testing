class ArithmeticOperations:

    def add(self, a, b):
        """
        Add two numbers together.

        Args:
            a (int): The first number.
            b (int): The second number.

        Returns:
            int: The sum of a and b.
        """
        return a + b

    def subtract(self, a, b):
        """
        Subtract the second number from the first number.

        Args:
            a (int): The first number.
            b (int): The second number.

        Returns:
            int: The difference between a and b.
        """
        return a - b

    def multiply(self, a, b):
        """
        Multiply two numbers.

        Args:
            a (int): The first number.
            b (int): The second number.

        Returns:
            int: The product of a and b.
        """
        return a * b

    def divide(self, a, b):
        """
        Divide the first number by the second number.

        Args:
            a (int): The first number.
            b (int): The second number.

        Returns:
            float: The result of a divided by b.

        Raises:
            ValueError: If b is zero.
        """
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b

    def power(self, a, b):
        """
        Raise the first number to the power of the second number.

        Args:
            a (int): The base number.
            b (int): The exponent.

        Returns:
            int: The result of a raised to the power of b.
        """
        return a ** b
