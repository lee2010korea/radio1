radio.onReceivedNumber(function (receivedNumber) {
    rkdnlqkdnlqh = randint(1, 3)
    _2 = receivedNumber
    if (rkdnlqkdnlqh == 1) {
        basic.showLeds(`
            # . . . #
            # . . . #
            . # . # .
            . # . # .
            . . # . .
            `)
    } else if (rkdnlqkdnlqh == 2) {
        basic.showLeds(`
            . . # . .
            . # # # .
            # # # # #
            . # # # .
            . . # . .
            `)
    } else if (rkdnlqkdnlqh == 3) {
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
    }
    if (_2 == 1 && rkdnlqkdnlqh == 1) {
        basic.showString("regame")
        radio.sendValue("name", 1)
    } else if (_2 == 2 && rkdnlqkdnlqh == 2) {
        basic.showString("regame")
        radio.sendValue("name", 1)
    } else if (_2 == 3 && rkdnlqkdnlqh == 3) {
        basic.showString("regame")
        radio.sendValue("name", 1)
    }
    if (_2 == 1 && rkdnlqkdnlqh == 2) {
        basic.showString("win")
        radio.sendValue("name", 2)
    } else if (_2 == 2 && rkdnlqkdnlqh == 3) {
        basic.showString("win")
        radio.sendValue("name", 2)
    } else if (_2 == 3 && rkdnlqkdnlqh == 1) {
        basic.showString("win")
        radio.sendValue("name", 2)
    }
    if (_2 == 2 && rkdnlqkdnlqh == 1) {
        basic.showString("fail")
        radio.sendValue("name", 3)
    } else if (_2 == 3 && rkdnlqkdnlqh == 1) {
        basic.showString("fail")
        radio.sendValue("name", 3)
    } else if (_2 == 1 && rkdnlqkdnlqh == 3) {
        basic.showString("fail")
        radio.sendValue("name", 3)
    }
    basic.pause(100)
})
input.onButtonPressed(Button.A, function () {
    game.addScore(1)
    basic.pause(100)
    basic.showNumber(game.score())
})
input.onGesture(Gesture.Shake, function () {
    rkdnlqkdnlqh = randint(1, 3)
    if (rkdnlqkdnlqh == 1) {
        basic.showLeds(`
            # . . . #
            # . . . #
            . # . # .
            . # . # .
            . . # . .
            `)
        radio.sendNumber(1)
    } else if (rkdnlqkdnlqh == 2) {
        basic.showLeds(`
            . . # . .
            . # # # .
            # # # # #
            . # # # .
            . . # . .
            `)
        radio.sendNumber(2)
    } else if (rkdnlqkdnlqh == 3) {
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        radio.sendNumber(3)
    }
})
radio.onReceivedValue(function (name, value) {
    _3 = value
    if (_3 == 1) {
        basic.showString("regame")
        basic.clearScreen()
    } else if (_3 == 2) {
        basic.showString("fail")
        basic.clearScreen()
    } else if (_3 == 3) {
        basic.showString("win")
        basic.clearScreen()
    }
})
let _3 = 0
let _2 = 0
let rkdnlqkdnlqh = 0
game.setScore(0)
