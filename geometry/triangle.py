from .basics import Point, GetDistance, Areas, General

class Triangle:

  def __init__(self, A: Point, B: Point, C: Point):
    self.A = A
    self.B = B
    self.C = C
    
    self.points = self.get_points()
    
    self.lengths = self.get_side_lengths()
    
    self.perimeter = General.get_perimeter(self.lengths)
    
    self.area = Areas.Triangle.Heron(self.lengths)

  def get_side_lengths(self) -> list:
    # The side is named after the letter of its opposing corner, lowercased
    c: float = GetDistance.between_points(self.A, self.B)
    a: float = GetDistance.between_points(self.B, self.C)
    b: float = GetDistance.between_points(self.A, self.C)
    
    return [c, a, b] # Returns AB, then BC, then AC

  def get_points(self) -> list:
    A = self.A.format
    B = self.B.format
    C = self.C.format
    
    return [A, B, C]

  def __str__(self) -> str:
    res: str = f"TRIANGLE defined with corners {self.points}."
    return res