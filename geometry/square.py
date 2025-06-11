from basics import Point
from math import sqrt

class Square:

  def __init__(self, A: Point, B: Point, C: Point, D: Point):
    self.A = A
    self.B = B
    self.C = C
    self.D = D
    
    self.points = self.get_points(self)
    
    if not self.check_validity(self):
      raise Exception(f"The points provided don't form a square. {self.points}")
    self.length = sqrt(((self.A.x - self.B.x) ** 2) + (self.A.y - self.B.y) ** 2)
    self.get_area(self)

  def get_area(self) -> float:
    if not self.check_validity(self):
      return
    return self.length ** 2

  def get_side_lengths(self) -> list:
    AB: float = sqrt(((self.A.x - self.B.x) ** 2) + (self.A.y - self.B.y) ** 2)
    BC: float = sqrt(((self.B.x - self.C.x) ** 2) + (self.B.y - self.C.y) ** 2)
    CD: float = sqrt(((self.C.x - self.D.x) ** 2) + (self.C.y - self.D.y) ** 2)
    AD: float = sqrt(((self.A.x - self.D.x) ** 2) + (self.A.y - self.D.y) ** 2)
    
    return [AB, BC, CD, AD]

  def check_validity(self) -> bool:
    [AB, BC, CD, AD] = self.get_side_lengths(self)
    
    return AB == BC == CD == AD

  def get_points(self) -> list:
    A = f"A({self.A.x}; {self.A.y})"
    B = f"({self.B.x}; {self.B.y})"
    C = f"({self.C.x}; {self.C.y})"
    D = f"({self.D.x}; {self.D.y})"
    
    return [A, B, C, D]