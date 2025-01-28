import os
import turtle
import argparse
from PIL import Image, ImageDraw
from tkinter import Tk, Canvas, Button

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

# start simulation
def start_simulation():
    global running, paused
    if not running:  # can be run only once
        running = True
        paused = False
        langton()

# pause simulation
def pause_simulation():
    global paused
    if running:
        paused = True

# resume simulation
def resume_simulation():
    global paused
    if running and paused:
        paused = False

# exporting image
def save_image():
    global draw,img
    # sciezka dla windowsa
    if os.name == 'nt':  # Windows
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    else:  # mac/Linux
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    output_path = os.path.join(desktop_path, "langton_grid.png")

    img.save(output_path, "PNG")
    print(f"Image saved as {output_path}")

# Tkinter window
root = Tk()
root.title("Mrówka Langtona")

# Canvas widget for Turtle
canvas = Canvas(root, width=600, height=600)
canvas.pack()

# Window settings
num_of_cells = 30
step = 10
window = turtle.TurtleScreen(canvas)
window_size = num_of_cells * step
window.bgcolor('white')
window.setworldcoordinates(-window_size, -window_size, window_size, window_size)

# Initialize the ant and the map
ant = Ant()
map = Map()

# Visualization of the map
field_turtle = turtle.RawTurtle(window)
field_turtle.shape('square')
field_turtle.shapesize(0.5)
field_turtle.hideturtle()

# visualization of the ant
ant_turtle = turtle.RawTurtle(window)
ant_turtle.shape('square')
ant_turtle.shapesize(0.5)
ant_turtle.color("red")
ant_turtle.penup()

# start stop resume buttons
start_button = Button(root, text="Start", command=start_simulation)
start_button.pack()

pause_button = Button(root, text="Pause", command=pause_simulation)
pause_button.pack()

resume_button = Button(root, text="Resume", command=resume_simulation)
resume_button.pack()

image_button = Button(root, text="Save image", command=save_image)
image_button.pack()

# buttons funcs setup
running = False
paused = False

img = Image.new("RGB", (window_size * 2, window_size * 2), color="white")
draw = ImageDraw.Draw(img)


def langton():
    global running, paused, draw

    while True:     # simulatiob loop
        if paused:
            window.update()
            continue
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

            draw.rectangle([current_position[0] + window_size, current_position[1] + window_size,
                            current_position[0] + window_size + step, current_position[1] + window_size + step], fill="black")
        else:
            # Turn left and change field color to white
            field_turtle.fillcolor("white")
            map.invert_color(current_position)
            ant.turn_left()

            draw.rectangle([current_position[0] + window_size, current_position[1] + window_size,
                            current_position[0] + window_size + step, current_position[1] + window_size + step], fill="white")
        field_turtle.stamp()

        # ant forward move
        ant.move_forward(step)

        # update ant pos
        ant_turtle.goto(ant.position)


root.mainloop()