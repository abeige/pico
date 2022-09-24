from machine import ADC, Timer
from time import sleep

temp_sensor = ADC(4)
timer = Timer()
to_volts = 3.3 / 65535

interval = 5
temps = []

def read_temp(timer):
    temp = temp_sensor.read_u16()
    temp_volts = temp * to_volts
    celsius_degrees = 27 - (temp_volts - 0.706) / 0.001721
    fahrenheit_degrees = celsius_degrees * 9 / 5 + 32
    temps.append(fahrenheit_degrees)
    print(f"{fahrenheit_degrees:.2f}")

timer.init(freq=5, mode=Timer.PERIODIC, callback=read_temp)
sleep(interval)
timer.deinit()

avg = sum(temps) / len(temps)
print(f"Average temp over {interval} seconds: {avg:.2f}")