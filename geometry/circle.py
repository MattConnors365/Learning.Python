from .basics import Point, Areas, General, GetDistance
from math import pi

class Circle:
  def __init__(self, center_point: Point, radius: float):
    self.center = center_point
    self.radius = radius

    self.circumference = pi * (self.radius * 2)
    self.area = Areas.Circle.area(self.radius)
