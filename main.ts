basic.forever(function on_forever() {
    led.plot(0, 0)
    
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showArrow(ArrowNames.North)
})
