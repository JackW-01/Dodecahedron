from random import randint
from random import seed
import math
import arcade

WIDTH = 800
HEIGHT = 600

window = arcade.Window(WIDTH, HEIGHT, "Bootleg Aimbooster")
arcade.set_background_color(arcade.color.WHITE)

# Initialize your variables here
cx = WIDTH//2
cy = HEIGHT//2
cr = 50
score = 0
textScore = str(score)


@window.event("on_draw")
def game_loop():
    # import global variables here.
    global cx
    global cy
    global cr
    global score
    global textScore
    # update your variables here.
    textScore = str(score)
    # Draw things here.
    arcade.start_render()
    arcade.draw_circle_filled(cx, cy, cr, arcade.color.ORANGE_PEEL)
    arcade.draw_text(textScore, 30, HEIGHT-20, arcade.color.BLACK, 14)


@window.event
def on_mouse_press(mox, moy, button, modifiers):
    # Import global variables
    global cr
    global cx
    global cy
    global score
    sideA = max(cx - mox, mox - cx)
    sideB = max(cy - moy, moy - cy)
    distance = math.sqrt(sideA * sideA + sideB * sideB)
    # Update variables
    if distance <= cr:
        score += 1
        for _ in range(1):
            cr = randint(20, 80)
            cx = randint(5, WIDTH-5)
            cy = randint(5, HEIGHT-5)
    else:
        score -= 2147483647
    print(f"Location. x: {mox}, y: {moy}")
    print(f"Distance: {distance} Radius: {cr}")


arcade.run()
