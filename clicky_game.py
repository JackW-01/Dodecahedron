from random import randint
from random import seed
import math
import arcade

WIDTH = 800
HEIGHT = 600

window = arcade.Window(WIDTH, HEIGHT, "Bootleg Aimbooster")
arcade.set_background_color(arcade.color.WHITE)

# Initialize your variables here
cx = WIDTH // 2 + 30
cy = HEIGHT // 2 + 30
cr = 7
cx_ = WIDTH // 2 - 30
cy_ = HEIGHT // 2 - 30
cr_ = 7
score = 0
textScore = f"Score: {score}"
instructions = "Click the Circles! (Speed = more points!)"


@window.event("on_draw")
def game_loop():
    # import global variables here.
    global cx
    global cy
    global cr
    global cx_
    global cy_
    global cr_
    global score
    global textScore
    # update your variables here.
    textScore = f"Score: {score}"
    cr += 0.065
    cr_ += 0.065
    if cr >= 25 or cr_ >= 25:
        score -= 4
        if cr >= 25:
            cr = 7
            cx = randint(15, WIDTH-15)
            cy = randint(15, HEIGHT-30)
        elif cr_ >= 25:
            cr_ = 7
            cx_ = randint(15, WIDTH-15)
            cy_ = randint(15, HEIGHT-30)
    # Draw things here.
    arcade.start_render()
    arcade.draw_circle_filled(cx, cy, cr, arcade.color.ORANGE_PEEL)
    arcade.draw_circle_filled(cx_, cy_, cr_, arcade.color.RED_ORANGE)
    arcade.draw_text(textScore, 50, HEIGHT-20, arcade.color.BLACK, 14)
    arcade.draw_text(instructions, 500, HEIGHT-20, arcade.color.BLACK, 12)


@window.event
def on_mouse_press(mox, moy, button, modifiers):
    # Import global variables
    global cr
    global cx
    global cy
    global cx_
    global cy_
    global cr_
    global score
    sideA = max(cx - mox, mox - cx)
    sideB = max(cy - moy, moy - cy)
    distance = math.sqrt(sideA * sideA + sideB * sideB)
    sideA = max(cx_ - mox, mox - cx_)
    sideB = max(cy_ - moy, moy - cy_)
    distance_ = math.sqrt(sideA * sideA + sideB * sideB)
    # Update variables
    if distance <= cr:
        if cr <= 14:
            score += 3
        else:
            score += 1
        cr = 7
        cx = randint(15, WIDTH-15)
        cy = randint(15, HEIGHT-30)
    elif distance_ <= cr_:
        if cr <= 14:
            score += 3
        else:
            score += 1
        cr_ = 7
        cx_ = randint(15, WIDTH-15)
        cy_ = randint(15, HEIGHT-30)
    else:
        score -= 2


arcade.run()
