import turtle
import argparse

class Ant:
    def __init__(self, start_position=(0, 0), start_direction=0):
        """
        Initializes the ant.
        """
        self.position = start_position  # (x, y)
        self.direction = start_direction  # 0 - up, 90 - right, 180 - down, 270 - left

    def move_forward(self, step):
        """
        Moves the ant forward in the current direction.
        """
        x, y = self.position
        if self.direction == 0:
            y += step
        elif self.direction == 90:
            x += step
        elif self.direction == 180:
            y -= step
        elif self.direction == 270:
            x -= step
        self.position = (x, y)

    def turn_right(self):
        """Ant turns right"""
        self.direction = (self.direction + 90) % 360

    def turn_left(self):
        """Ant turns left"""
        self.direction = (self.direction - 90) % 360

class Map:
    def __init__(self):
        """Initializes the map"""
        self.grid = {}  # dict storing field colors

    def get_color(self, position):
        """Returns the color of the field on the map. Default is white."""
        return self.grid.get(position, "white")

    def invert_color(self, position):
        """
        Inverts the color of the field to its opposite.
        """
        current_color = self.get_color(position)
        new_color = "black" if current_color == "white" else "white"
        self.grid[position] = new_color
        return new_color

def langton(color, step, num_of_cells):
    # Window settings
    window_size = num_of_cells * step
    window = turtle.Screen()
    window.bgcolor('white')
    window.setup(width=window_size * 2, height=window_size * 2)
    window.setworldcoordinates(-window_size, -window_size, window_size, window_size)

    # Initialize the ant and the map
    ant = Ant()
    world_map = Map()

    # Visualization of the map
    field_turtle = turtle.Turtle()
    field_turtle.shape('square')
    field_turtle.shapesize(0.5)
    field_turtle.hideturtle()

    # Visualization of the ant
    ant_turtle = turtle.Turtle()
    ant_turtle.shape('triangle')
    ant_turtle.color(color)
    ant_turtle.penup()

    # Simulation loop
    for _ in range(num_of_cells * num_of_cells):
        current_position = ant.position
        current_color = world_map.get_color(current_position)

        # Update map
        field_turtle.penup()
        field_turtle.goto(current_position)
        if current_color == "white":
            field_turtle.fillcolor("black")
            ant.turn_right()
        else:
            field_turtle.fillcolor("white")
            ant.turn_left()
        world_map.invert_color(current_position)
        field_turtle.stamp()

        # Move ant forward
        ant.move_forward(step)
        ant_turtle.goto(ant.position)

    turtle.mainloop()

if __name__ == "__main__":
    """argumenty, które zmieniają wygląd planszy i mrówki"""
    parser = argparse.ArgumentParser(description="Symulacja mrówki Langtona")
    parser.add_argument("--color", type=str, default="purple")
    parser.add_argument("--step", type=int, default=10)
    parser.add_argument("--cells", type=int, default=30)

    args = parser.parse_args()
    langton(args.color, args.step, args.cells)

