from .basics import Point, GetDistance, Areas, General


class Triangle:
    """Represents a triangle defined by three corner points.

    Attributes:
        A (Point): The first corner point of the triangle.
        B (Point): The second corner point of the triangle.
        C (Point): The third corner point of the triangle.
        points (list[str]): A list of formatted string representations of the corner points.
        lengths (list[float]): A list containing the lengths of the three sides.
        perimeter (float): The perimeter of the triangle.
        area (float): The area of the triangle, calculated using Heron's formula.
    """

    def __init__(self, A: Point, B: Point, C: Point):
        """Initializes a Triangle object with three corner points.

        Args:
            A (Point): The first corner point.
            B (Point): The second corner point.
            C (Point): The third corner point.
        """
        self.A = A
        self.B = B
        self.C = C

        self.points = self.get_points()

        self.lengths = self.get_side_lengths()

        self.perimeter = General.get_perimeter(self.lengths)

        self.area = Areas.Triangle.Heron(self.lengths)

    def get_side_lengths(self) -> list[float]:
        """Calculates the lengths of the three sides of the triangle.

        Sides are named after the letter of their opposing corner, lowercased (a=BC, b=AC, c=AB).

        Returns:
            list[float]: A list containing the lengths of sides c (AB), a (BC), and b (AC) in that order.
        """
        # The side is named after the letter of its opposing corner, lowercased
        c: float = GetDistance.between_points(self.A, self.B)  # Side opposite C
        a: float = GetDistance.between_points(self.B, self.C)  # Side opposite A
        b: float = GetDistance.between_points(self.A, self.C)  # Side opposite B

        return [c, a, b]  # Returns AB, then BC, then AC

    def get_points(self) -> list[str]:
        """Gets the formatted string representations of the triangle's corner points.

        Returns:
            list[str]: A list of strings, each representing a corner point (e.g., "A(0; 0)").
        """
        A = self.A.format
        B = self.B.format
        C = self.C.format

        return [A, B, C]

    def __str__(self) -> str:
        """Returns a string representation of the Triangle object.

        Returns:
            str: A descriptive string including the corner points of the triangle.
        """
        res: str = f"TRIANGLE defined with corners {self.points}."
        return res