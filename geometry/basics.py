from math import sqrt, fsum, pi

class Point:
  def __init__(self, letter: chr, x_coordinate: float, y_coordinate: float):
    self._letter = letter
    self._x = x_coordinate
    self._y = y_coordinate
  
  def __str__(self) -> str:
    return self.format
  
  
  @property
  def letter(self) -> chr:
    return self._letter
  @letter.setter
  def letter(self, value: chr) -> None:
    self._letter = value
  
  @property
  def x(self) -> float:
    return self._x
  @x.setter
  def x(self, value: float) -> None:
    self._x = value
  
  @property
  def y(self) -> float:
    return self._y
  @y.setter
  def y(self, value: float) -> None:
    self._y = value
    
  @property
  def format(self) -> str:
    return f"{self.letter}({self.x}; {self.y})"

class MiddlePoint(Point):
  def __init__(self, letter: chr,  A: Point, B: Point):
    super().__init__(letter, 0, 0)
    self.x = (A.x + B.x) / 2
    self.y = (A.y + B.y) / 2

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

  class Circle:
    @staticmethod
    def area(radius: float) -> float:
      return pi * radius ** 2
