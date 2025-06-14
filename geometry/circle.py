from .basics import Point, Areas, GetDistance
from math import pi, sqrt

class Circle:
  def __init__(self, center_point: Point, radius: float):
    self._center = center_point
    self._radius = radius

  def contains(self, check: Point, include_points_on_boundary: bool = True) -> bool:
    distance_between_center_and_check = GetDistance.between_points(self.center, check)
    return distance_between_center_and_check <= self.radius if include_points_on_boundary \
      else distance_between_center_and_check < self.radius
  
  def __str__(self) -> str:
    res: str = f"CIRCLE defined with center {self.center} and a radius of {self.radius}."
    return res
  
  @property
  def center(self) -> Point:
    return self._center
  @center.setter
  def center(self, value: Point) -> None:
    self._center = value
  
  @property
  def radius(self) -> float:
    return self._radius
  @radius.setter
  def radius(self, value: float) -> None:
    if value < 0:
      raise ValueError("Radius can't be negative")
    self._radius = value

  @property
  def diameter(self) -> float:
    return self.radius * 2
  @diameter.setter
  def diameter(self, value: float) -> None:
    if value < 0:
      raise ValueError("Diameter can't be negative")
    self.radius = value / 2

  @property
  def circumference(self) -> float:
    return self.diameter * pi
  @circumference.setter
  def circumference(self, value: float) -> None:
    if value < 0:
      raise ValueError("Circumference can't be negative")
    self.radius = (value / pi) / 2

  @property
  def area(self) -> float:
    return Areas.Circle.area(self.radius)
  @area.setter
  def area(self, value: float) -> None:
    if value < 0:
      raise ValueError("Area can't be negative")
    self.radius = sqrt(value / pi)


