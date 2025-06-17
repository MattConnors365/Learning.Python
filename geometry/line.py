# geometry/line.py
from __future__ import annotations

class Line:
    """Represents a line in a 2D coordinate system.

    A line is defined by the general equation Ax + By + C = 0.

    Attributes:
        a (float): The coefficient 'A' in the line equation.
        b (float): The coefficient 'B' in the line equation.
        c (float): The coefficient 'C' in the line equation.
    """
    def __init__(self, a: float, b: float, c: float):
        """Initializes a Line object.

        Args:
            a (float): The coefficient 'A' from the line equation Ax + By + C = 0.
            b (float): The coefficient 'B' from the line equation Ax + By + C = 0.
            c (float): The coefficient 'C' from the line equation Ax + By + C = 0.
        """
        self.a = a
        self.b = b
        self.c = c

    @property
    def a(self) -> float:
        """Gets the 'A' coefficient of the line equation.

        Returns:
            float: The 'A' coefficient.
        """
        return self._a
    @a.setter
    def a(self, value: float) -> None:
        """Sets the 'A' coefficient of the line equation.

        Args:
            value (float): The new 'A' coefficient.
        """
        self._a = value

    @property
    def b(self) -> float:
        """Gets the 'B' coefficient of the line equation.

        Returns:
            float: The 'B' coefficient.
        """
        return self._b
    @b.setter
    def b(self, value: float) -> None:
        """Sets the 'B' coefficient of the line equation.

        Args:
            value (float): The new 'B' coefficient.
        """
        self._b = value

    @property
    def c(self) -> float:
        """Gets the 'C' coefficient of the line equation.

        Returns:
            float: The 'C' coefficient.
        """
        return self._c
    @c.setter
    def c(self, value: float) -> None:
        """Sets the 'C' coefficient of the line equation.

        Args:
            value (float): The new 'C' coefficient.
        """
        self._c = value

    @property
    def slope(self) -> float:
        """Calculates the slope of the line.

        Returns:
            float: The slope of the line. Returns `float('inf')` for vertical lines.
        """
        if self.b != 0:
            return -self.a / self.b
        return float('inf')  # Vertical line

    def __str__(self) -> str:
        """Returns a string representation of the line equation.

        Returns:
            str: A formatted string representing the line equation (e.g., "x + y + 5 = 0").
        """
        parts = []

        # Handle 'ax' term
        if self.a != 0:
            if self.a == 1:
                parts.append("x")
            elif self.a == -1:
                parts.append("-x")
            else:
                parts.append(f"{self.a}x")

        # Handle 'by' term
        if self.b != 0:
            if self.b > 0:
                if parts:  # If there's already an 'ax' term, add a " + "
                    parts.append(" + ")
                if self.b == 1:
                    parts.append("y")
                else:
                    parts.append(f"{self.b}y")
            else:  # self.b < 0
                if parts:  # If there's already an 'ax' term, add a " - "
                    parts.append(" - ")
                if self.b == -1:
                    parts.append("y")
                else:
                    parts.append(f"{abs(self.b)}y")  # Use abs for negative, as '-' is added separately

        # Handle 'c' term
        if self.c != 0:
            if self.c > 0:
                if parts:  # If there's already an 'ax' or 'by' term, add a " + "
                    parts.append(" + ")
                parts.append(f"{self.c}")
            else:  # self.c < 0
                if parts:  # If there's already an 'ax' or 'by' term, add a " - "
                    parts.append(" - ")
                parts.append(f"{abs(self.c)}")  # Use abs for negative, as '-' is added separately

        if not parts:
            return "0 = 0"  # Case where a, b, c are all zero

        return f"{''.join(parts)} = 0"

    @classmethod
    def from_points(cls, A: 'Point', B: 'Point'):
        """Creates a Line object from two given Point objects.

        This class method calculates the coefficients (A, B, C) of the line
        equation Ax + By + C = 0 that passes through the two specified points.

        Args:
            A (Point): The first point.
            B (Point): The second point.

        Returns:
            Line: A new Line object defined by the two points.
        """
        a = A.y - B.y
        b = B.x - A.x
        c = A.x * B.y - B.x * A.y
        return cls(a, b, c)

    def distance_to_point(self, P: 'Point') -> float:
        """Calculates the shortest distance from this line to a given point.

        Args:
            P (Point): The point to which the distance is to be calculated.

        Returns:
            float: The perpendicular distance from the line to the point.
        """
        from .basics import GetDistance
        return GetDistance.point_to_line(P, self)

    def contains_point(self, P: 'Point') -> bool:
        """Checks if a given point lies on this line.

        Args:
            P (Point): The point to check.

        Returns:
            bool: True if the point is on the line, False otherwise.
        """
        return (self.a * P.x + self.b * P.y + self.c) == 0

    def is_perpendicular(self, other: 'Line') -> bool:
        """Checks if this line is perpendicular to another line.

        Args:
            other (Line): The other Line object to compare against.

        Returns:
            bool: True if the lines are perpendicular, False otherwise.
        """
        if self.slope is float('inf') and other.slope == 0:
            return True
        if self.slope == 0 and other.slope is float('inf'):
            return True
        # Handle cases where one or both slopes are undefined (vertical lines)
        if self.b == 0 and other.a == 0:  # self is vertical, other is horizontal
            return True
        if self.a == 0 and other.b == 0:  # self is horizontal, other is vertical
            return True

        # Standard case: product of slopes is -1
        return self.slope * other.slope == -1

    def is_parallel(self, other: 'Line') -> bool:
        """Checks if this line is parallel to another line.

        Args:
            other (Line): The other Line object to compare against.

        Returns:
            bool: True if the lines are parallel, False otherwise.
        """
        if self.slope is float('inf') and other.slope is float('inf'):
            return True
        return self.slope == other.slope