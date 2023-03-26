import math


class GeometryCalculations:
    """
    A class that provides simple geometry calculation methods.
    """

    @staticmethod
    def rectangle_area(width: float, height: float) -> float:
        """
        Calculate the area of a rectangle.

        :param width: The width of the rectangle
        :param height: The height of the rectangle
        :return: The area of the rectangle
        """
        if width < 0 or height < 0:
            raise ValueError("Width and height must be non-negative")
        return width * height

    @staticmethod
    def triangle_area(base: float, height: float) -> float:
        """
        Calculate the area of a triangle.

        :param base: The base of the triangle
        :param height: The height of the triangle
        :return: The area of the triangle
        """
        if base < 0 or height < 0:
            raise ValueError("Base and height must be non-negative")
        return 0.5 * base * height

    @staticmethod
    def circle_area(radius: float) -> float:
        """
        Calculate the area of a circle.

        :param radius: The radius of the circle
        :return: The area of the circle
        """
        if radius < 0:
            raise ValueError("Radius must be non-negative")
        return math.pi * radius ** 2

    @staticmethod
    def circle_circumference(radius: float) -> float:
        """
        Calculate the circumference of a circle.

        :param radius: The radius of the circle
        :return: The circumference of the circle
        """
        if radius < 0:
            raise ValueError("Radius must be non-negative")
        return 2 * math.pi * radius

    @staticmethod
    def can_form_triangle(a: float, b: float, c: float) -> bool:
        """
        Check if three points form a triangle.

        :param a: The length of the first side
        :param b: The length of the second side
        :param c: The length of the third side
        :return: True if the three points form a triangle, False otherwise
        """
        if a < 0 or b < 0 or c < 0:
            raise ValueError("Triangle side lengths must be non-negative")
        return a + b > c and a + c > b and b + c > a
