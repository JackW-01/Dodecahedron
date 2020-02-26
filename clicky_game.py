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
cr = 7
score = 0
textScore = f"Score: {score}"
instructions = "Click the Circles! (Speed = more points!)"


@window.event("on_draw")
def game_loop():
    # import global variables here.
    global cx
    global cy
    global cr
    global score
    global textScore
    # update your variables here.
    textScore = f"Score: {score}"
    cr += 0.04
    if cr >= 40:
        cr = 7
        score -= 2
        for _ in range(1):
            cx = randint(15, WIDTH-15)
            cy = randint(15, HEIGHT-15)
    # Draw things here.
    arcade.start_render()
    arcade.draw_circle_filled(cx, cy, cr, arcade.color.ORANGE_PEEL)
    arcade.draw_text(textScore, 50, HEIGHT-20, arcade.color.BLACK, 14)
    arcade.draw_text(instructions, 500, HEIGHT-20, arcade.color.BLACK, 12)


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
        if cr <= 12:
            score += 3
        else:
            score += 1
        cr = 7
        for _ in range(1):
            cx = randint(15, WIDTH-15)
            cy = randint(15, HEIGHT-15)
    else:
        score -= 2
    print(f"Location. x: {mox}, y: {moy}")
    print(f"Distance: {distance} Radius: {cr}")


arcade.run()
