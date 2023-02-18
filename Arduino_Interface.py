import serial
import time

from gameLib import *

arduino = serial.Serial(port='COM8', baudrate=115200, timeout=.1)


def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data


while True:
    num = world.score
    value = write_read(num)
    print(value)