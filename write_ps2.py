import machine
import time
from machine import Pin

ps2_data = Pin(10, Pin.OUT, Pin.PULL_UP)

def write_f():
    ps2_data.off()
    time.sleep_us(40)
    ps2_data.on()
    time.sleep_us(80)
    ps2_data.off()
    time.sleep_us(40)
    ps2_data.on()
    time.sleep_us(40)
    ps2_data.off()
    time.sleep_us(40)
    ps2_data.on()
    time.sleep_us(40)
    ps2_data.off()
    time.sleep_us(80)
    ps2_data.on()
    time.sleep_us(80)

for i in range(1000):
    time.sleep_us(100)
    write_f()