from random import randint
import math
import arcade

WIDTH = 800
HEIGHT = 600

window = arcade.Window(WIDTH, HEIGHT, "Bad Target Smasher")
arcade.set_background_color(arcade.color.LIGHT_SLATE_GRAY)

# Initialize your variables here
cx = randint(25, WIDTH - 25); cy = randint(25, HEIGHT - 70); cr = 7         # This is Circle 1
cx_ = randint(25, WIDTH - 25); cy_ = randint(25, HEIGHT - 70); cr_ = 7      # This is Circle 2
_cx = randint(25, WIDTH - 25); _cy = randint(25, HEIGHT - 70); _cr = 9      # This is the evil Circle
score = 0
misses = 10
textDisplay: str
instructions = "Click the Circles! (Speed = More Points!)"
instructions1 = "Avoid Clicking the Black Circle! (Lose Points!)"


@window.event("on_draw")
def game_loop():
    global cx, cy, cr, cx_, cy_, cr_, score, textDisplay, misses, _cx, _cy, _cr
    ''' Update your variables here. '''
    if score < 0: score = 0
    textDisplay = f"Score: {score}        Misses Left: {misses}"
    # When the radius >= 24: miss and circle re-appears
    if cr >= 24:
        misses -= 1
        cr = 7
        cx = randint(25, WIDTH - 25)
        cy = randint(25, HEIGHT - 70)
    elif cr_ >= 24:
        misses -= 1
        cr_ = 7
        cx_ = randint(25, WIDTH - 25)
        cy_ = randint(25, HEIGHT - 70)
    elif _cr >= 24:
        _cr = 9
        _cx = randint(25, WIDTH - 25)
        _cy = randint(25, HEIGHT - 70)
    # When score >= 150 or 300 circles grow faster
    if score >= 300:
        cr_ += 0.1
        cr += 0.1
        _cr += 0.07
    elif score >= 150:
        cr_ += 0.08
        cr += 0.08
        _cr += 0.055
    else:
        cr_ += 0.065
        cr += 0.065
        _cr += 0.04
    # When you have 0 misses left, the game ends
    if misses <= 0: exit()
    ''' Draw things here '''
    arcade.start_render()
    arcade.draw_circle_filled(cx, cy, cr, arcade.color.ORANGE_PEEL)                 # Circle one
    arcade.draw_circle_filled(cx_, cy_, cr_, arcade.color.RED_ORANGE)               # Circle two
    arcade.draw_circle_filled(_cx, _cy, _cr, arcade.color.EERIE_BLACK)              # Evil Circle
    arcade.draw_text(textDisplay, 10, HEIGHT - 20, arcade.color.BLACK, 14)          # Points and Misses
    arcade.draw_text(instructions, 510, HEIGHT - 20, arcade.color.BLACK, 12)        # Instructions
    arcade.draw_text(instructions1, 477, HEIGHT - 40, arcade.color.BLACK, 12)       # More instructions


@window.event
def on_mouse_press(mox, moy, button, modifiers):
    global cr, cx, cy, cx_, cy_, cr_, score, misses, _cx, _cy, _cr
    """ Define variables here """
    sideA = abs(cx - mox); sideB = abs(cy - moy); distance = math.sqrt(sideA ** 2 + sideB ** 2)
    sideA = abs(cx_ - mox); sideB = abs(cy_ - moy); distance_ = math.sqrt(sideA ** 2 + sideB ** 2)
    sideA = abs(_cx - mox); sideB = abs(_cy - moy); _distance = math.sqrt(sideA ** 2 + sideB ** 2)
    ''' Update variables here '''
    if distance <= cr:          # Circle one
        if cr <= 13:
            score += 3
        else:
            score += 1
        cr = 7
        cx = randint(25, WIDTH - 25)
        cy = randint(25, HEIGHT - 70)
    elif distance_ <= cr_:      # Circle two
        if cr <= 13:
            score += 3
        else:
            score += 1
        cr_ = 7
        cx_ = randint(25, WIDTH - 25)
        cy_ = randint(25, HEIGHT - 70)
    elif _distance <= _cr:      # Evil Circle
        score -= 10
        misses -= 1
        _cr = 9
        _cx = randint(25, WIDTH - 25)
        _cy = randint(25, HEIGHT - 70)
    else:
        misses -= 1


arcade.run()
