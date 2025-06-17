"""Demonstrates the usage of geometric classes from the mathcraft project.

This script initializes various geometric shapes (Square, Triangle, Circle) and
a Line, then prints out some of their properties and performs basic operations.
It serves as an example of how to interact with the `geometry` package.
"""

from geometry.basics import Point
from geometry.square import Square
from geometry.triangle import Triangle
from geometry.circle import Circle
from geometry.line import Line

if __name__ == '__main__':
    # Define points for geometric constructions
    A: Point = Point('A', 0, 0)
    B: Point = Point('B', 0, 4)
    C: Point = Point('C', 4, 4)
    D: Point = Point('D', 4, 0)

    # Demonstrate Square operations
    print("--- Square Demonstration ---")
    sq = Square(A, B, C, D)
    print(f"Square points: {sq.points}")
    print(f"Square object: {sq}")
    print(f"Square side length: {sq.lengths[0]:.2f}")
    print(f"Square area: {sq.area:.2f}")

    # Demonstrate Triangle operations
    print("\n--- Triangle Demonstration ---")
    tr = Triangle(A, B, C)
    print(f"Triangle object: {tr}")
    print(f"Triangle side lengths: {[f'{l:.2f}' for l in tr.lengths]}")
    print(f"Triangle area: {tr.area:.2f}")
    print(f"Triangle perimeter: {tr.perimeter:.2f}")

    # Demonstrate Circle operations
    print("\n--- Circle Demonstration ---")
    cr = Circle(A, 5)  # Circle centered at A with radius 5
    print(f"Circle object: {cr}")
    print(f"Circle radius: {cr.radius:.2f}")
    print(f"Circle area: {cr.area:.2f}")
    print(f"Circle center: {cr.center}")
    print(f"Circle circumference: {cr.circumference:.2f}")

    # Demonstrate Line operations
    print("\n--- Line Demonstration ---")
    ln = Line.from_points(B, D)  # Line passing through B and D
    print(f"Line object: {ln}")
    print(f"Does line contain point B? {ln.contains_point(B)}")
    print(f"Does line contain point A? {ln.contains_point(A)}")  # A (0,0) will not be on line B(0,4)-D(4,0)