from random import randint
import math
import arcade

WIDTH = 800
HEIGHT = 600

window = arcade.Window(WIDTH, HEIGHT, "Bootleg Aimbooster")
arcade.set_background_color(arcade.color.LIGHT_SLATE_GRAY)

# Initialize your variables here
cx = randint(15, WIDTH-15)
cy = randint(15, HEIGHT-30)
cr = 7
cx_ = randint(15, WIDTH-15)
cy_ = randint(15, HEIGHT-30)
cr_ = 7
score = 0
misses = 10
textScore: str
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
    global misses
    # update your variables here.
    textScore = f"Score: {score}        Misses Left: {misses}"
    if cr >= 25:
        misses -= 1
        cr = 7
        cx = randint(15, WIDTH-15)
        cy = randint(15, HEIGHT-30)
    elif cr_ >= 25:
        misses -= 1
        cr_ = 7
        cx_ = randint(15, WIDTH-15)
        cy_ = randint(15, HEIGHT-30)
    cr_ += 0.065
    cr += 0.065
    if misses < 0:
        exit()
    # Draw things here.
    arcade.start_render()
    arcade.draw_circle_filled(cx, cy, cr, arcade.color.ORANGE_PEEL)
    arcade.draw_circle_filled(cx_, cy_, cr_, arcade.color.RED_ORANGE)
    arcade.draw_text(textScore, 10, HEIGHT-20, arcade.color.BLACK, 14)
    arcade.draw_text(instructions, 510, HEIGHT-20, arcade.color.BLACK, 12)


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
    global misses
    sideA = abs(cx - mox)
    sideB = abs(cy - moy)
    distance = math.sqrt(sideA ** 2 + sideB ** 2)
    sideA = abs(cx_ - mox)
    sideB = abs(cy_ - moy)
    distance_ = math.sqrt(sideA ** 2 + sideB ** 2)
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
        misses -= 1


arcade.run()
