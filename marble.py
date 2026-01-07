
from point import Point
import turtle

class Marble:
    def __init__(self, position: Point, color: str, radius: int = 15):
        self.position = position
        self.color = color
        self.radius = radius

    def draw(self):
        turtle.penup()
        turtle.goto(self.position.x, self.position.y - self.radius)
        turtle.pendown()
        turtle.fillcolor(self.color)
        turtle.begin_fill()
        turtle.circle(self.radius)
        turtle.end_fill()
        turtle.penup()

    def __repr__(self):
        return f"Marble(position={self.position}, color='{self.color}')"
