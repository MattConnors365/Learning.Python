# geometry/basics.py
from __future__ import annotations
from math import sqrt, fsum, pi


class Point:
    """Represents a point in a 2D coordinate system.

    Attributes:
        letter (chr): The letter designation for the point (e.g., 'A', 'B').
        x (float): The x-coordinate of the point.
        y (float): The y-coordinate of the point.
    """

    def __init__(self, letter: chr, x_coordinate: float, y_coordinate: float):
        """Initializes a Point object.

        Args:
            letter (chr): The letter designation for the point (e.g., 'A', 'B').
            x_coordinate (float): The x-coordinate of the point.
            y_coordinate (float): The y-coordinate of the point.
        """
        self.letter = letter
        self.x = x_coordinate
        self.y = y_coordinate

    @classmethod
    def MiddlePoint(cls, letter: chr, A: Point, B: Point) -> Point:
        """Initializes a Point object with coordinates in the middle of points A and B.

        Args:
            letter (chr): The letter designation for the middle point.
            A (Point): The first point.
            B (Point): The second point.
        """
        x: float = (A.x + B.x) / 2
        y: float = (A.y + B.y) / 2
        return cls(letter, x, y)

    def __str__(self) -> str:
        """Returns a string representation of the Point.

        Returns:
            str: A formatted string representing the point, e.g., "A(0; 0)".
        """
        return self.format

    @property
    def letter(self) -> chr:
        """Gets the letter designation of the point.

        Returns:
            chr: The letter of the point.
        """
        return self._letter

    @letter.setter
    def letter(self, value: chr) -> None:
        """Sets the letter designation of the point.

        Args:
            value (chr): The new letter for the point.
        """
        self._letter = value

    @property
    def x(self) -> float:
        """Gets the x-coordinate of the point.

        Returns:
            float: The x-coordinate.
        """
        return self._x

    @x.setter
    def x(self, value: float) -> None:
        """Sets the x-coordinate of the point.

        Args:
            value (float): The new x-coordinate.
        """
        self._x = value

    @property
    def y(self) -> float:
        """Gets the y-coordinate of the point.

        Returns:
            float: The y-coordinate.
        """
        return self._y

    @y.setter
    def y(self, value: float) -> None:
        """Sets the y-coordinate of the point.

        Args:
            value (float): The new y-coordinate.
        """
        self._y = value

    @property
    def format(self) -> str:
        """Gets the formatted string representation of the point.

        Returns:
            str: A string like "A(0; 0)".
        """
        return f"{self.letter}({self.x}; {self.y})"


class GetDistance:
    """A collection of static methods for calculating distances between geometrical entities."""

    @staticmethod
    def between_points(A: Point, B: Point) -> float:
        """Calculates the Euclidean distance between two points.

        Args:
            A (Point): The first point.
            B (Point): The second point.

        Returns:
            float: The distance between point A and point B.
        """
        return sqrt(((A.x - B.x) ** 2) + (A.y - B.y) ** 2)

    @staticmethod
    def point_to_line(P: Point, L: 'Line') -> float:
        """Calculates the shortest distance from a point to a line.

        Args:
            P (Point): The point.
            L (Line): The line, represented in the form Ax + By + C = 0.

        Returns:
            float: The perpendicular distance from the point to the line.

        Raises:
            TypeError: If L is not an instance of the Line class.
        """
        from .line import Line
        if not isinstance(L, Line):
            raise TypeError("L must be an instance of Line")
        return abs(L.a * P.x + L.b * P.y + L.c) / sqrt(L.a ** 2 + L.b ** 2)


class General:
    """A collection of general utility methods for mathematical concepts."""

    @staticmethod
    def get_perimeter(arr: list) -> float:
        """Calculates the perimeter from a list of side lengths.

        Args:
            arr (list): A list of numerical values representing side lengths.

        Returns:
            float: The sum of all lengths in the list.
        """
        return fsum(arr)


class Areas:
    """A collection of static methods for calculating areas of various geometrical shapes."""

    class Square:
        """Static methods for square area calculations."""

        @staticmethod
        def area(length: float) -> float:
            """Calculates the area of a square given its side length.

            Args:
                length (float): The length of one side of the square.

            Returns:
                float: The area of the square.
            """
            return length ** 2

    class Triangle:
        """Static methods for triangle area calculations."""

        @staticmethod
        def Heron(lengths: list) -> float:
            """Calculates the area of a triangle using Heron's formula.

            Args:
                lengths (list): A list containing the three side lengths of the triangle.

            Returns:
                float: The area of the triangle.
            """
            [a, b, c] = lengths
            semi_perimeter: float = (a + b + c) / 2
            p = semi_perimeter
            return sqrt(p * (p - a) * (p - b) * (p - c))

        @staticmethod
        def RightTriangle(leg1: float, leg2: float) -> float:
            """Calculates the area of a right-angled triangle.

            Args:
                leg1 (float): The length of the first leg.
                leg2 (float): The length of the second leg.

            Returns:
                float: The area of the right triangle.
            """
            return (leg1 * leg2) / 2

    class Circle:
        """Static methods for circle area calculations."""

        @staticmethod
        def area(radius: float) -> float:
            """Calculates the area of a circle given its radius.

            Args:
                radius (float): The radius of the circle.

            Returns:
                float: The area of the circle.
            """
            return pi * radius ** 2