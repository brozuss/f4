import turtle
import time

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

        Functionality:
        - Updates the (x, y) coordinates based on the current direction (`self.direction`):
          - If `self.direction == 0` (up): Increases `y` by `step`.
          - If `self.direction == 90` (right): Increases `x` by `step`.
          - If `self.direction == 180` (down): Decreases `y` by `step`.
          - If `self.direction == 270` (left): Decreases `x` by `step`.
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
            - Black to White
            - White to Black
        """
        current_color = self.get_color(position)
        new_color = "black" if current_color == "white" else "white"
        self.grid[position] = new_color
        return new_color


def langton():
    # Window settings
    num_of_cells = 30
    step = 10
    window_size = num_of_cells * step
    window = turtle.Screen()
    window.bgcolor('white')
    window.setup(width=window_size * 2, height=window_size * 2)  # Set window size
    window.setworldcoordinates(-window_size, -window_size, window_size, window_size)

    # Initialize the ant and the map
    ant = Ant()
    map = Map()

    # Visualization of the map
    field_turtle = turtle.Turtle()
    field_turtle.shape('square')
    field_turtle.shapesize(0.5)
    field_turtle.hideturtle()

    # visualization of the ant
    ant_turtle = turtle.Turtle()
    ant_turtle.shape('square')
    ant_turtle.shapesize(0.5)
    ant_turtle.color("red")
    ant_turtle.penup()

    # initializes step counter
    step_count = 0

    # Create a turtle to display the step count
    step_counter_turtle = turtle.Turtle()
    step_counter_turtle.penup()
    step_counter_turtle.hideturtle()
    step_counter_turtle.goto(0, window_size + 200)
    step_counter_turtle.color("black")
    step_counter_turtle.write(f"Step count: {step_count}", align="center", font=("Arial", 16, "normal"))

    # simulatiob loop
    while True:
        current_position = ant.position
        current_color = map.get_color(current_position)

        # Update map
        field_turtle.penup()
        field_turtle.goto(current_position)
        if current_color == "white":
            # Turn right and change field color to black
            field_turtle.fillcolor("black")
            map.invert_color(current_position)
            ant.turn_right()
        else:
            # Turn left and change field color to white
            field_turtle.fillcolor("white")
            map.invert_color(current_position)
            ant.turn_left()
        field_turtle.stamp()

        # ant forward move
        ant.move_forward(step)

        # update ant pos
        ant_turtle.goto(ant.position)

        # increases steps count
        step_count += 1

        # Update the step count display
        step_counter_turtle.clear()
        step_counter_turtle.write(f"Step count: {step_count}", align="center", font=("Arial", 16, "normal"))

        # pause for a while
        time.sleep(0.001)

langton()
