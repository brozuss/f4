import os
import turtle
import argparse
from PIL import Image, ImageDraw
from tkinter import Tk, Canvas, Button, Label
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

        map_hsize = map_size //2

        # Zapętlanie pozycji (modulo w zakresie [-half_grid, half_grid])
        if x > map_hsize:
            x = -map_hsize + 1
        elif x < -map_hsize:
            x = map_hsize - 1

        if y > map_hsize:
            y = -map_hsize + 1
        elif y < -map_hsize:
            y = map_hsize - 1

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
        border_turtle = turtle.RawTurtle(window)
        border_turtle.hideturtle()
        border_turtle.penup()
        border_turtle.pencolor("red")  # Kolor obramowania
        border_turtle.pensize(3)  # Grubość linii

        map_hsize = map_size //2

        # Przesunięcie do narożnika i rysowanie
        border_turtle.goto(-map_hsize, -map_hsize)
        border_turtle.pendown()
        for _ in range(4):
            border_turtle.forward(map_size)
            border_turtle.left(90)
        border_turtle.penup()

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


def langton():
    global running, paused, draw, step_count, speed, step

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

            draw.rectangle([current_position[0] + map_size, current_position[1] + map_size,
                            current_position[0] + map_size + step, current_position[1] + map_size + step], fill="black")
        else:
            # Turn left and change field color to white
            field_turtle.fillcolor("white")
            map.invert_color(current_position)
            ant.turn_left()

            draw.rectangle([current_position[0] + map_size, current_position[1] + map_size,
                            current_position[0] + map_size + step, current_position[1] + map_size + step], fill="white")
        field_turtle.stamp()

        # ant forward move
        ant.move_forward(10)

        # update ant pos
        ant_turtle.goto(ant.position)

        # increases steps count
        step_count += 1
        step_button.config(text=f"kroki: {step_count}")

        # pause for a while
        time.sleep(speed)

if __name__ == "__main__":
    """argumenty, które zmieniają wygląd planszy i mrówki"""
    parser = argparse.ArgumentParser(description="Symulacja mrówki Langtona")
    parser.add_argument("--color", type=str, default="purple")
    parser.add_argument("--size", type=int, default=600)
    parser.add_argument("--speed", type=float, default=0.01)
    args = parser.parse_args()
    color=args.color
    map_size=args.size
    speed=args.speed

# Tkinter window
root = Tk()
root.title("Mrówka Langtona")

# Canvas widget for Turtle
canvas = Canvas(root, width=map_size, height=map_size)
canvas.pack()

# Window settings
# num_of_cells = 30
step = 10
window = turtle.TurtleScreen(canvas)
window.bgcolor('white')
window.setworldcoordinates(-map_size//2, -map_size//2, map_size//2, map_size//2)

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
ant_turtle.color(color)
ant_turtle.penup()

# initializes step counter
step_count = 0

# start stop resume buttons
# button_frame = Canvas(root)
# button_frame.pack(padx=5, pady=5)

step_button = Label(root, text=f"kroki: {step_count}", font=("Arial",15))
step_button.pack(side="left", padx=90, pady=5)

start_button = Button(root, text="Start", command=start_simulation)
start_button.pack(side="right", padx=10, pady=5)

pause_button = Button(root, text="Pause", command=pause_simulation)
pause_button.pack(side="right", padx=10, pady=5)

resume_button = Button(root, text="Resume", command=resume_simulation)
resume_button.pack(side="right", padx=10, pady=5)

image_button = Button(root, text="Save image", command=save_image)
image_button.pack(side="right", padx=10, pady=5)

# buttons funcs setup
running = False
paused = False

img = Image.new("RGB", (map_size * 2, map_size * 2), color="white")
draw = ImageDraw.Draw(img)

root.mainloop()