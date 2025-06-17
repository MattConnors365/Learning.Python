from .basics import Point, GetDistance, Areas, General
from math import sqrt, isclose


class Square:
    """Represents a square defined by four corner points.

    A square is validated upon initialization to ensure the provided points
    form a true square (all sides equal length).

    Attributes:
        A (Point): The first corner point of the square.
        B (Point): The second corner point of the square.
        C (Point): The third corner point of the square.
        D (Point): The fourth corner point of the square.
        points (list[str]): A list of formatted string representations of the corner points.
        lengths (list[float]): A list containing the lengths of the four sides.
        perimeter (float): The perimeter of the square.
        area (float): The area of the square.
    """

    def __init__(self, A: Point, B: Point, C: Point, D: Point):
        """Initializes a Square object with four corner points.

        Args:
            A (Point): The first corner point.
            B (Point): The second corner point.
            C (Point): The third corner point.
            D (Point): The fourth corner point.

        Raises:
            Exception: If the provided points do not form a valid square.
        """
        self.A = A
        self.B = B
        self.C = C
        self.D = D

        self.points = self.get_points()

        if not self.check_validity():
            raise Exception(f"The points provided don't form a square. {self.points}")

        self.lengths = self.get_side_lengths()

        self.perimeter = General.get_perimeter(self.lengths)

        self.area = Areas.Square.area(self.lengths[0])

    def get_side_lengths(self) -> list[float]:
        """Calculates the lengths of the four sides of the square.

        Returns:
            list[float]: A list containing the lengths of sides AB, BC, CD, and AD.
        """
        AB: float = GetDistance.between_points(self.A, self.B)
        BC: float = GetDistance.between_points(self.B, self.C)
        CD: float = GetDistance.between_points(self.C, self.D)
        AD: float = GetDistance.between_points(self.A, self.D)

        return [AB, BC, CD, AD]

    def check_validity(self) -> bool:
        """Checks if the four provided points form a valid square.

        This is determined by checking if all side lengths are approximately equal.

        Returns:
            bool: True if the points form a square, False otherwise.
        """
        [AB, BC, CD, AD] = self.get_side_lengths()

        return all(isclose(side, AB, rel_tol=1e-9) for side in [BC, CD, AD])

    def get_points(self) -> list[str]:
        """Gets the formatted string representations of the square's corner points.

        Returns:
            list[str]: A list of strings, each representing a corner point (e.g., "A(0; 0)").
        """
        A = self.A.format
        B = self.B.format
        C = self.C.format
        D = self.D.format

        return [A, B, C, D]

    def __str__(self) -> str:
        """Returns a string representation of the Square object.

        Returns:
        str: A descriptive string including the corner points of the square.
        """
        res: str = f"SQUARE defined with corners {self.points}."
        return res