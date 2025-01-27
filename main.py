import os
import turtle
import argparse
from PIL import Image, ImageDraw

class Ant:
    def __init__(self, start_position=(0, 0), start_direction=0):
        self.position = start_position
        self.direction = start_direction

    def move_forward(self, step):
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
        self.direction = (self.direction + 90) % 360

    def turn_left(self):
        self.direction = (self.direction - 90) % 360


class Map:
    def __init__(self):
        self.grid = {}

    def get_color(self, position):
        return self.grid.get(position, "white")

    def invert_color(self, position):
        current_color = self.get_color(position)
        new_color = "black" if current_color == "white" else "white"
        self.grid[position] = new_color
        return new_color


def langton(num_moves):
    num_of_cells = 30
    step = 10
    window_size = num_of_cells * step

    # sciezka dla windowsa
    if os.name == 'nt':  # Windows
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    else:  # mac/Linux
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")


    output_path = os.path.join(desktop_path, "langton_grid.png")

    img = Image.new("RGB", (window_size * 2, window_size * 2), color="white")
    draw = ImageDraw.Draw(img)

    ant = Ant()
    map = Map()

    for _ in range(num_moves):
        current_position = ant.position
        current_color = map.get_color(current_position)

        # Determine the color based on the grid state
        if current_color == "white":
            draw.rectangle([current_position[0] + window_size, current_position[1] + window_size,
                            current_position[0] + window_size + step, current_position[1] + window_size + step], fill="black")
            map.invert_color(current_position)
            ant.turn_right()
        else:
            draw.rectangle([current_position[0] + window_size, current_position[1] + window_size,
                            current_position[0] + window_size + step, current_position[1] + window_size + step], fill="white")
            map.invert_color(current_position)
            ant.turn_left()

        ant.move_forward(step)

    # zapisuje obrazek
    img.save(output_path, "PNG")
    print(f"Image saved as {output_path}")


def parse_arguments():
    parser = argparse.ArgumentParser(description="Simulate Langton's Ant.")
    parser.add_argument("num_moves", type=int, help="Number of moves for the ant to make.")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    langton(args.num_moves)
