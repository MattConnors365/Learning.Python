from __future__ import annotations

class Line:
  def __init__(self, a: float, b: float, c: float):
    self.a = a
    self.b = b
    self.c = c

  @property
  def slope(self):
    if self.b != 0:
      return -self.a / self.b
    return float('inf')  # Vertical line

  def __str__(self):
    a_sign = "- " if self.a < 0 else ""
    a = f"{a_sign}{abs(self.a)}" if self.a != 0 else ""
    b_sign = " - " if self.b < 0 else " + "
    b = f"{b_sign}{abs(self.b)}" if self.b != 0 else "0"
    c_sign = " - " if self.c < 0 else " + "
    c = f"{c_sign}{abs(self.c)}" if self.c != 0 else ""
    return f"{a}x{b}y{c} = 0"

  @classmethod
  def from_points(cls, A: Point, B: Point):
    from .basics import Point
    a = A.y - B.y
    b = B.x - A.x
    c = A.x * B.y - B.x * A.y
    return cls(a, b, c)

  def distance_to_point(self, P: Point) -> float:
    from .basics import Point, GetDistance
    return GetDistance.point_to_line(P, self)

  def contains_point(self, P: Point) -> bool:
    from .basics import Point
    return True if (self.a * P.x + self.b * P.y + self.c) == 0 else False

  def is_perpendicular(self, other: Line) -> bool:
    return True if self.slope * other.slope == -1 else False

  def is_parallel(self, other: Line) -> bool:
    return True if self.slope == other.slope else False

