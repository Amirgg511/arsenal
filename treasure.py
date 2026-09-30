import pgzrun
from random import randint
from time import time

WIDTH = 1000
HEIGHT = 400

points = []
lines = []
next_point = 0

start_time = 0
total_time = 0

number_of_points = 8


def create_points():
    global start_time

    for count in range(number_of_points):
        point = Actor("ponterr")

        point.pos = (
            randint(50, WIDTH - 50),
            randint(50, HEIGHT - 50)
        )

        points.append(point)

    start_time = time()


def draw():
    global total_time

    # Draw the map
    screen.blit("map", (0, 0))

    number = 1

    # Draw all the treasure points
    for point in points:

        screen.draw.text(
            str(number),
            (point.x + 20, point.y - 35),
            fontsize=25,
            color="black"
        )

        point.draw()

        number = number + 1

    # Draw the trail
    for line in lines:
        screen.draw.line(
            line[0],
            line[1],
            (80, 40, 10)
        )

    # Timer
    if next_point < number_of_points:
        total_time = time() - start_time

    screen.draw.text(
        "Time: " + str(round(total_time, 1)),
        (10, 10),
        fontsize=25,
        color="black"
    )

    # You found the treasure!
    if next_point == number_of_points:
        screen.draw.text(
            "TREASURE FOUND!",
            (350, 20),
            fontsize=35,
            color="black"
        )


def update():
    pass


def on_mouse_down(pos):
    global next_point, lines

    if next_point < number_of_points:

        # Did we click the correct point?
        if points[next_point].collidepoint(pos):

            # Draw a line from the previous point
            if next_point > 0:
                lines.append((
                    points[next_point - 1].pos,
                    points[next_point].pos
                ))

            next_point = next_point + 1

        else:
            # Wrong point, start again
            lines = []
            next_point = 0


create_points()

pgzrun.go()