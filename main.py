from window import Window
from line import Line
from point import Point

def main():
    window = Window(800, 600)
    point1 = Point(100, 100)
    point2 = Point(200, 500)
    point3 = Point(300, 300)
    line = Line(point1, point2)
    line2 = Line(point2, point3)
    window.draw_line(line, "red")
    window.draw_line(line2, "blue")

    window.wait_for_close()

if __name__ == "__main__":
    main()
