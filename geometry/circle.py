from .basics import Point, Areas, GetDistance
from math import pi, sqrt


class Circle:
    """Represents a circle defined by a center point and a radius.

    Attributes:
        _center (Point): The center point of the circle.
        _radius (float): The radius of the circle.
    """

    def __init__(self, center_point: Point, radius: float):
        """Initializes a Circle object.

        Args:
            center_point (Point): The center point of the circle.
            radius (float): The radius of the circle.
        """
        self._center = center_point
        self._radius = radius

    def contains(self, check: Point, include_points_on_boundary: bool = True) -> bool:
        """Checks if a given point is inside or on the boundary of the circle.

        Args:
            check (Point): The point to check for containment.
            include_points_on_boundary (bool): If True, points exactly on the
                circle's circumference are considered inside. Defaults to True.

        Returns:
            bool: True if the point is contained within (or on) the circle, False otherwise.
        """
        distance_between_center_and_check = GetDistance.between_points(self.center, check)
        return distance_between_center_and_check <= self.radius if include_points_on_boundary \
            else distance_between_center_and_check < self.radius

    def __str__(self) -> str:
        """Returns a string representation of the Circle object.

        Returns:
            str: A descriptive string including the center and radius of the circle.
        """
        res: str = f"CIRCLE defined with center {self.center} and a radius of {self.radius}."
        return res

    @property
    def center(self) -> Point:
        """Gets the center point of the circle.

        Returns:
            Point: The center Point object.
        """
        return self._center

    @center.setter
    def center(self, value: Point) -> None:
        """Sets the center point of the circle.

        Args:
            value (Point): The new center Point object.
        """
        self._center = value

    @property
    def radius(self) -> float:
        """Gets the radius of the circle.

        Returns:
            float: The radius value.
        """
        return self._radius

    @radius.setter
    def radius(self, value: float) -> None:
        """Sets the radius of the circle.

        Args:
            value (float): The new radius value.

        Raises:
            ValueError: If the provided radius is negative.
        """
        if value < 0:
            raise ValueError("Radius can't be negative")
        self._radius = value

    @property
    def diameter(self) -> float:
        """Gets the diameter of the circle.

        Returns:
            float: The diameter value (twice the radius).
        """
        return self.radius * 2

    @diameter.setter
    def diameter(self, value: float) -> None:
        """Sets the diameter of the circle, which updates the radius.

        Args:
            value (float): The new diameter value.

        Raises:
            ValueError: If the provided diameter is negative.
        """
        if value < 0:
            raise ValueError("Diameter can't be negative")
        self.radius = value / 2

    @property
    def circumference(self) -> float:
        """Gets the circumference of the circle.

        Returns:
            float: The circumference value (diameter * pi).
        """
        return self.diameter * pi

    @circumference.setter
    def circumference(self, value: float) -> None:
        """Sets the circumference of the circle, which updates the radius.

        Args:
            value (float): The new circumference value.

        Raises:
            ValueError: If the provided circumference is negative.
        """
        if value < 0:
            raise ValueError("Circumference can't be negative")
        self.radius = (value / pi) / 2

    @property
    def area(self) -> float:
        """Gets the area of the circle.

        Returns:
            float: The area value (pi * radius^2).
        """
        return Areas.Circle.area(self.radius)

    @area.setter
    def area(self, value: float) -> None:
        """Sets the area of the circle, which updates the radius.

        Args:
            value (float): The new area value.

        Raises:
            ValueError: If the provided area is negative.
        """
        if value < 0:
            raise ValueError("Area can't be negative")
        self.radius = sqrt(value / pi)