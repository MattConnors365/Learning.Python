from math import sqrt

class Point:
  def __init__(self, letter: chr, x_coordinate: float, y_coordinate: float):
    self.letter = letter
    self.x = x_coordinate
    self.y = y_coordinate
    self.format = self.return_format()
  def return_format(self):
    return f"{self.letter}({self.x}; {self.y})"

class MiddlePoint(Point):
  def __init__(self, letter: chr,  A: Point, B: Point):
    super().__init__(letter, 0, 0)
    self.x = (A.x + B.x) / 2
    self.y = (A.y + B.y) / 2
    self.format = self.return_format()

class GetDistance:
  @staticmethod
  def between_points(A: Point, B: Point) -> float:
    return sqrt(((A.x - B.x) ** 2) + (A.y - B.y) ** 2)
