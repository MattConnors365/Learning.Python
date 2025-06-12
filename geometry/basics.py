from math import sqrt, fsum

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
  
class General:
  @staticmethod
  def get_perimeter(arr: list):
    return fsum(arr)
  
class Areas:
  class Square:
    @staticmethod
    def area(length: float) -> float:
      return length ** 2
    
  class Triangle:
    @staticmethod
    def Heron(lengths: list) -> float:
      [a, b, c] = lengths
      semi_perimeter: float = (a + b + c) / 2
      p = semi_perimeter
      return sqrt(p * (p - a) * (p - b) * (p - c))
    
    @staticmethod
    def RightTriangle(leg1: float, leg2: float) -> float:
      return (leg1 * leg2) / 2