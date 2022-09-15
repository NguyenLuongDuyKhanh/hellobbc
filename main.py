def on_forever():
    led.plot(0, 0)
    pass

basic.forever(on_forever)

basic.show_string("Hello!")
def on_forever2():
    pass
basic.forever(on_forever2)