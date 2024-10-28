player = 0
hand = 0

def on_button_pressed_a():
    global player
    basic.clear_screen()
    basic.show_leds("""
        . . # . .
        . # # # .
        # # # # #
        . # # # .
        . . # . .
        """)
    player = 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    global hand
    hand = randint(1, 3)
    if hand == 1:
        basic.clear_screen()
        basic.show_leds("""
            . . # . .
            . # # # .
            # # # # #
            . # # # .
            . . # . .
            """)
    if hand == 2:
        basic.clear_screen()
        basic.show_leds("""
            . # # # .
            . # # # .
            . # # # .
            . # # # .
            . # # # .
            """)
    if hand == 3:
        basic.clear_screen()
        basic.show_icon(IconNames.SCISSORS)
    if hand == player:
        basic.show_icon(IconNames.ASLEEP)
    else:
        if hand == 3 and player == 1 or hand < player and player - hand == 1:
            basic.show_icon(IconNames.HAPPY)
        else:
            basic.show_icon(IconNames.SAD)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_ab():
    global player
    basic.clear_screen()
    basic.show_icon(IconNames.SCISSORS)
    player = 3
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global player
    basic.clear_screen()
    basic.show_leds("""
        . # # # .
        . # # # .
        . # # # .
        . # # # .
        . # # # .
        """)
    player = 2
input.on_button_pressed(Button.B, on_button_pressed_b)
