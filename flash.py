from machine import Pin, Timer
led = Pin("LED", Pin.OUT)
timer = Timer()

def blink(timer):
    led.toggle()

def stop():
    timer.deinit()
    led.off()

timer.init(freq=2.5, mode=Timer.PERIODIC, callback=blink)
