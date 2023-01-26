input.onPinPressed(TouchPin.P0, function () {
    basic.showString("" + randint(0, 99))
})
basic.forever(function () {
    if (input.buttonIsPressed(Button.A)) {
        if (18 >= input.temperature() && input.temperature() < 20) {
            basic.showLeds(`
                . . # . .
                . # # # .
                # # # # #
                . # # # .
                . . # . .
                `)
        } else if (22 < input.temperature() && input.temperature() >= 24) {
            basic.showLeds(`
                . . # . .
                . . # . .
                . # # # .
                . # # # .
                # # # # #
                `)
        } else {
            basic.showLeds(`
                . . . . .
                . . . . #
                . . . # .
                # . # . .
                . # . . .
                `)
        }
    } else if (input.buttonIsPressed(Button.B)) {
        if (input.lightLevel() > 20) {
            basic.showString("Bright!!!")
        } else {
            basic.showString("dark")
        }
    } else if (input.buttonIsPressed(Button.A) && input.buttonIsPressed(Button.B)) {
        if (input.magneticForce(Dimension.X) + input.magneticForce(Dimension.Y) + input.magneticForce(Dimension.Z) > 100) {
            basic.showString("Mag")
        }
    }
})
