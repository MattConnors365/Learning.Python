from geometry import Point, Square

if __name__ == '__main__':
  A: Point = Point('A', 0, 0)
  B: Point = Point('B', 0, 4)
  C: Point = Point('C', 4, 0)
  D: Point = Point('D', 4, 4)
  
  sq = Square(A, B, C, D)
  print(sq.points)