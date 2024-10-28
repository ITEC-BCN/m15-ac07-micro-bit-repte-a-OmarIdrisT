let player = 0
let hand = 0
input.onButtonPressed(Button.A, function () {
    basic.clearScreen()
    basic.showLeds(`
        . . # . .
        . # # # .
        # # # # #
        . # # # .
        . . # . .
        `)
    player = 1
})
input.onGesture(Gesture.Shake, function () {
    hand = randint(1, 3)
    if (hand == 1) {
        basic.clearScreen()
        basic.showLeds(`
            . . # . .
            . # # # .
            # # # # #
            . # # # .
            . . # . .
            `)
    }
    if (hand == 2) {
        basic.clearScreen()
        basic.showLeds(`
            . # # # .
            . # # # .
            . # # # .
            . # # # .
            . # # # .
            `)
    }
    if (hand == 3) {
        basic.clearScreen()
        basic.showIcon(IconNames.Scissors)
    }
    if (hand == player) {
        basic.showIcon(IconNames.Asleep)
    } else {
        if (hand == 3 && player == 1 || hand < player && player - hand == 1) {
            basic.showIcon(IconNames.Happy)
        } else {
            basic.showIcon(IconNames.Sad)
        }
    }
})
input.onButtonPressed(Button.AB, function () {
    basic.clearScreen()
    basic.showIcon(IconNames.Scissors)
    player = 3
})
input.onButtonPressed(Button.B, function () {
    basic.clearScreen()
    basic.showLeds(`
        . # # # .
        . # # # .
        . # # # .
        . # # # .
        . # # # .
        `)
    player = 2
})
