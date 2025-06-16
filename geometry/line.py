# geometry/line.py
from __future__ import annotations

class Line:
  def __init__(self, a: float, b: float, c: float):
    self._a = a
    self._b = b
    self._c = c

  @property
  def a(self):
    return self._a
  @a.setter
  def a(self, value):
    self._a = value

  @property
  def b(self):
    return self._b
  @b.setter
  def b(self, value):
    self._b = value

  @property
  def c(self):
    return self._c
  @c.setter
  def c(self, value):
    self._c = value

  @property
  def slope(self):
    if self.b != 0:
        return -self.a / self.b
    return float('inf')  # Vertical line

  def __str__(self):
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
    a = A.y - B.y
    b = B.x - A.x
    c = A.x * B.y - B.x * A.y
    return cls(a, b, c)

  def distance_to_point(self, P: 'Point') -> float:
    from .basics import GetDistance
    return GetDistance.point_to_line(P, self)

  def contains_point(self, P: 'Point') -> bool:
    return (self.a * P.x + self.b * P.y + self.c) == 0

  def is_perpendicular(self, other: 'Line') -> bool:
    if self.slope is float('inf') and other.slope == 0:
      return True
    if self.slope == 0 and other.slope is float('inf'):
      return True
    # Handle cases where one or both slopes are undefined (vertical lines)
    if self.b == 0 and other.a == 0:  # self is vertical, other is horizontal
      return True
    if self.a == 0 and other.b == 0:  # self is horizontal, other is vertical
      return True

    # Standard case
    return self.slope * other.slope == -1

  def is_parallel(self, other: Line) -> bool:
    if self.slope is float('inf') and other.slope is float('inf'):
      return True
    return self.slope == other.slope