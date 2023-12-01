def on_received_number(receivedNumber):
    global rkdnlqkdnlqh, _2
    rkdnlqkdnlqh = randint(1, 3)
    _2 = receivedNumber
    if rkdnlqkdnlqh == 1:
        basic.show_leds("""
            # . . . #
            # . . . #
            . # . # .
            . # . # .
            . . # . .
            """)
    elif rkdnlqkdnlqh == 2:
        basic.show_leds("""
            . . # . .
            . # # # .
            # # # # #
            . # # # .
            . . # . .
            """)
    elif rkdnlqkdnlqh == 3:
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
    if _2 == 1 and rkdnlqkdnlqh == 1:
        basic.show_string("regame")
        radio.send_value("name", 1)
    elif _2 == 2 and rkdnlqkdnlqh == 2:
        basic.show_string("regame")
        radio.send_value("name", 1)
    elif _2 == 3 and rkdnlqkdnlqh == 3:
        basic.show_string("regame")
        radio.send_value("name", 1)
    if _2 == 1 and rkdnlqkdnlqh == 2:
        basic.show_string("win")
        radio.send_value("name", 2)
    elif _2 == 2 and rkdnlqkdnlqh == 3:
        basic.show_string("win")
        radio.send_value("name", 2)
    elif _2 == 3 and rkdnlqkdnlqh == 1:
        basic.show_string("win")
        radio.send_value("name", 2)
    if _2 == 2 and rkdnlqkdnlqh == 1:
        basic.show_string("fail")
        radio.send_value("name", 3)
    elif _2 == 3 and rkdnlqkdnlqh == 1:
        basic.show_string("fail")
        radio.send_value("name", 3)
    elif _2 == 1 and rkdnlqkdnlqh == 3:
        basic.show_string("fail")
        radio.send_value("name", 3)
    basic.pause(100)
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    game.add_score(1)
    basic.pause(100)
    basic.show_number(game.score())
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    global rkdnlqkdnlqh
    rkdnlqkdnlqh = randint(1, 3)
    if rkdnlqkdnlqh == 1:
        basic.show_leds("""
            # . . . #
            # . . . #
            . # . # .
            . # . # .
            . . # . .
            """)
        radio.send_number(1)
    elif rkdnlqkdnlqh == 2:
        basic.show_leds("""
            . . # . .
            . # # # .
            # # # # #
            . # # # .
            . . # . .
            """)
        radio.send_number(2)
    elif rkdnlqkdnlqh == 3:
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        radio.send_number(3)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_received_value(name, value):
    global _3
    _3 = value
    if _3 == 1:
        basic.show_string("regame")
        basic.clear_screen()
    elif _3 == 2:
        basic.show_string("fail")
        basic.clear_screen()
    elif _3 == 3:
        basic.show_string("win")
        basic.clear_screen()
radio.on_received_value(on_received_value)

rkdnlqkdnlqh = 0
_3 = 0
_2 = 0
game.set_score(0)