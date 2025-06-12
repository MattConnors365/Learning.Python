from geometry.basics import Point
from geometry.square import Square
from geometry.triangle import Triangle

if __name__ == '__main__':
  A: Point = Point('A', 0, 0)
  B: Point = Point('B', 0, 4)
  C: Point = Point('C', 4, 4)
  D: Point = Point('D', 4, 0)
  
  sq = Square(A, B, C, D)
  print(sq.points)
  print(sq)
  print(sq.lengths[0])
  print(sq.area)
  
  tr = Triangle(A, B, C)
  print(tr)
  print(tr.lengths)
  print(tr.area)
  print(tr.perimeter)
  
