def on_forever():
    led.plot(0, 0)
    pass

basic.forever(on_forever)

def on_button_pressed_a():
    basic.show_arrow(ArrowNames.NORTH)
input.on_button_pressed(Button.A, on_button_pressed_a)