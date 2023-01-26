def on_pin_pressed_p0():
    basic.show_string("" + str(randint(0, 99)))
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_forever():
    if input.button_is_pressed(Button.A):
        if 18 >= input.temperature() and input.temperature() < 20:
            basic.show_leds("""
                . . # . .
                                . # # # .
                                # # # # #
                                . # # # .
                                . . # . .
            """)
        elif 22 < input.temperature() and input.temperature() >= 24:
            basic.show_leds("""
                . . # . .
                                . . # . .
                                . # # # .
                                . # # # .
                                # # # # #
            """)
        else:
            basic.show_leds("""
                . . . . .
                                . . . . #
                                . . . # .
                                # . # . .
                                . # . . .
            """)
    elif input.button_is_pressed(Button.B):
        if input.light_level() > 20:
            basic.show_string("Bright!!!")
        else:
            basic.show_string("dark")
    elif input.button_is_pressed(Button.A) and input.button_is_pressed(Button.B):
        if input.magnetic_force(Dimension.X)+input.magnetic_force(Dimension.Y)+input.magnetic_force(Dimension.Z) >100:
            basic.show_string("Mag")
basic.forever(on_forever)
