from .basics import Point, GetDistance, Areas, General
from math import sqrt, isclose

class Square:

  def __init__(self, A: Point, B: Point, C: Point, D: Point):
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

  def get_side_lengths(self) -> list:
    AB: float = GetDistance.between_points(self.A, self.B)
    BC: float = GetDistance.between_points(self.B, self.C)
    CD: float = GetDistance.between_points(self.C, self.D)
    AD: float = GetDistance.between_points(self.A, self.D)
    
    return [AB, BC, CD, AD]

  def check_validity(self) -> bool:
    [AB, BC, CD, AD] = self.get_side_lengths()
    
    return all(isclose(side, AB, rel_tol=1e-9) for side in [BC, CD, AD])

  def get_points(self) -> list:
    A = self.A.format
    B = self.B.format
    C = self.C.format
    D = self.D.format
    
    return [A, B, C, D]

  def __str__(self) -> str:
    res: str = f"SQUARE defined with corners {self.points}."
    return res
