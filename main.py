valor = 0

def on_button_pressed_a():
    basic.clear_screen()
    basic.show_leds("""
        . . # . .
        . # # # .
        # # # # #
        . # # # .
        . . # . .
        """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    global valor
    valor = randint(1, 3)
    if valor == 1:
        basic.clear_screen()
        basic.show_leds("""
            . . # . .
            . # # # .
            # # # # #
            . # # # .
            . . # . .
            """)
    if valor == 2:
        basic.clear_screen()
        basic.show_leds("""
            . # # # .
            . # # # .
            . # # # .
            . # # # .
            . # # # .
            """)
    if valor == 3:
        basic.clear_screen()
        basic.show_icon(IconNames.SCISSORS)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_ab():
    basic.clear_screen()
    basic.show_icon(IconNames.SCISSORS)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.clear_screen()
    basic.show_leds("""
        . # # # .
        . # # # .
        . # # # .
        . # # # .
        . # # # .
        """)
input.on_button_pressed(Button.B, on_button_pressed_b)
