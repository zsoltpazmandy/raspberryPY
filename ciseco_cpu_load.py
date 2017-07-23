import psutil
import time
import sys
import serial
from random import randint

serial = serial.Serial()
serial.baudrate = 9600
serial.timeout = 0
serial.port = "/dev/serial0"

tens_offset = 0
ones_offset = 7

idle_text = ["Zzz", "idle", "bored", "yawn", ":)", "hello?", "hola!", "doh", "erm..", "awake?"]
idle_threshold = 5


# function to initialise serial port and communication with the GPIO display
def init():
    try:
        serial.open()
    except serial.SerialException, exception:
        sys.stderr.write("Opening port %r failed: %s\n" % (serial.port, exception))
        sys.exit(1)


# function to turn all LEDs on on the display
def all_leds_on():
    serial.write("$$$ALL,ON\r")


# function to turn all LEDs off on the display
def all_leds_off():
    serial.write("$$$ALL,OFF\r")


def splash():
    all_leds_on()
    time.sleep(0.1)
    all_leds_off()
    serial.write("ready")
    time.sleep(2)


def zero(offset):
    serial.write("$$$P" + str(offset + 2) + ",2,ON\r")
    serial.write("$$$P" + str(offset + 2) + ",3,ON\r")
    serial.write("$$$P" + str(offset + 2) + ",4,ON\r")
    serial.write("$$$P" + str(offset + 2) + ",5,ON\r")
    serial.write("$$$P" + str(offset + 2) + ",6,ON\r")
    serial.write("$$$P" + str(offset + 2) + ",7,ON\r")
    serial.write("$$$P" + str(offset + 2) + ",8,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",1,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",2,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",3,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",4,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",5,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",6,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",7,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",8,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",9,ON\r")
    serial.write("$$$P" + str(offset + 4) + ",1,ON\r")
    serial.write("$$$P" + str(offset + 4) + ",9,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",1,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",2,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",3,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",4,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",5,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",6,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",7,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",8,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",9,ON\r")
    serial.write("$$$P" + str(offset + 6) + ",2,ON\r")
    serial.write("$$$P" + str(offset + 6) + ",3,ON\r")
    serial.write("$$$P" + str(offset + 6) + ",4,ON\r")
    serial.write("$$$P" + str(offset + 6) + ",5,ON\r")
    serial.write("$$$P" + str(offset + 6) + ",6,ON\r")
    serial.write("$$$P" + str(offset + 6) + ",7,ON\r")
    serial.write("$$$P" + str(offset + 6) + ",8,ON\r")
    return


def one(offset):
    serial.write("$$$P" + str(offset + 3) + ",2,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",3,ON\r")
    serial.write("$$$P" + str(offset + 4) + ",1,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",1,ON\r")
    serial.write("$$$P" + str(offset + 4) + ",2,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",2,ON\r")
    serial.write("$$$P" + str(offset + 4) + ",3,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",3,ON\r")
    serial.write("$$$P" + str(offset + 4) + ",4,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",4,ON\r")
    serial.write("$$$P" + str(offset + 4) + ",5,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",5,ON\r")
    serial.write("$$$P" + str(offset + 4) + ",6,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",6,ON\r")
    serial.write("$$$P" + str(offset + 4) + ",7,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",7,ON\r")
    serial.write("$$$P" + str(offset + 4) + ",8,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",8,ON\r")
    serial.write("$$$P" + str(offset + 4) + ",9,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",9,ON\r")
    serial.write("$$$P" + str(offset + 4) + ",8,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",8,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",9,ON\r")
    serial.write("$$$P" + str(offset + 4) + ",9,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",9,ON\r")
    serial.write("$$$P" + str(offset + 6) + ",9,ON\r")
    return


def two(offset):
    serial.write("$$$P" + str(offset + 2) + ",2,ON\r")
    serial.write("$$$P" + str(offset + 2) + ",3,ON\r")
    serial.write("$$$P" + str(offset + 2) + ",7,ON\r")
    serial.write("$$$P" + str(offset + 2) + ",8,ON\r")
    serial.write("$$$P" + str(offset + 2) + ",9,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",1,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",2,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",3,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",6,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",7,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",8,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",9,ON\r")
    serial.write("$$$P" + str(offset + 4) + ",1,ON\r")
    serial.write("$$$P" + str(offset + 4) + ",2,ON\r")
    serial.write("$$$P" + str(offset + 4) + ",5,ON\r")
    serial.write("$$$P" + str(offset + 4) + ",6,ON\r")
    serial.write("$$$P" + str(offset + 4) + ",8,ON\r")
    serial.write("$$$P" + str(offset + 4) + ",9,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",1,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",2,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",3,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",4,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",5,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",8,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",9,ON\r")
    serial.write("$$$P" + str(offset + 6) + ",2,ON\r")
    serial.write("$$$P" + str(offset + 6) + ",3,ON\r")
    serial.write("$$$P" + str(offset + 6) + ",4,ON\r")
    serial.write("$$$P" + str(offset + 6) + ",8,ON\r")
    serial.write("$$$P" + str(offset + 6) + ",9,ON\r")
    return


def three(offset):
    serial.write("$$$P" + str(offset + 2) + ",2,ON\r")
    serial.write("$$$P" + str(offset + 2) + ",3,ON\r")
    serial.write("$$$P" + str(offset + 2) + ",7,ON\r")
    serial.write("$$$P" + str(offset + 2) + ",8,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",1,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",2,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",3,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",7,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",8,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",9,ON\r")
    serial.write("$$$P" + str(offset + 4) + ",1,ON\r")
    serial.write("$$$P" + str(offset + 4) + ",5,ON\r")
    serial.write("$$$P" + str(offset + 4) + ",9,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",1,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",2,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",3,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",4,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",5,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",6,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",7,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",8,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",9,ON\r")
    serial.write("$$$P" + str(offset + 6) + ",2,ON\r")
    serial.write("$$$P" + str(offset + 6) + ",3,ON\r")
    serial.write("$$$P" + str(offset + 6) + ",4,ON\r")
    serial.write("$$$P" + str(offset + 6) + ",6,ON\r")
    serial.write("$$$P" + str(offset + 6) + ",7,ON\r")
    serial.write("$$$P" + str(offset + 6) + ",8,ON\r")
    return


def four(offset):
    serial.write("$$$P" + str(offset + 2) + ",1,ON\r")
    serial.write("$$$P" + str(offset + 2) + ",2,ON\r")
    serial.write("$$$P" + str(offset + 2) + ",3,ON\r")
    serial.write("$$$P" + str(offset + 2) + ",4,ON\r")
    serial.write("$$$P" + str(offset + 2) + ",5,ON\r")
    serial.write("$$$P" + str(offset + 2) + ",6,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",1,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",2,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",3,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",4,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",5,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",6,ON\r")
    serial.write("$$$P" + str(offset + 4) + ",6,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",5,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",6,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",7,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",8,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",9,ON\r")
    serial.write("$$$P" + str(offset + 6) + ",5,ON\r")
    serial.write("$$$P" + str(offset + 6) + ",6,ON\r")
    serial.write("$$$P" + str(offset + 6) + ",7,ON\r")
    serial.write("$$$P" + str(offset + 6) + ",8,ON\r")
    serial.write("$$$P" + str(offset + 6) + ",9,ON\r")
    return


def five(offset):
    serial.write("$$$P" + str(offset + 2) + ",1,ON\r")
    serial.write("$$$P" + str(offset + 2) + ",2,ON\r")
    serial.write("$$$P" + str(offset + 2) + ",3,ON\r")
    serial.write("$$$P" + str(offset + 2) + ",4,ON\r")
    serial.write("$$$P" + str(offset + 2) + ",5,ON\r")
    serial.write("$$$P" + str(offset + 2) + ",8,ON\r")
    serial.write("$$$P" + str(offset + 2) + ",9,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",1,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",2,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",3,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",4,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",5,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",8,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",9,ON\r")
    serial.write("$$$P" + str(offset + 4) + ",1,ON\r")
    serial.write("$$$P" + str(offset + 4) + ",5,ON\r")
    serial.write("$$$P" + str(offset + 4) + ",9,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",1,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",5,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",6,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",7,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",8,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",9,ON\r")
    serial.write("$$$P" + str(offset + 6) + ",1,ON\r")
    serial.write("$$$P" + str(offset + 6) + ",2,ON\r")
    serial.write("$$$P" + str(offset + 6) + ",5,ON\r")
    serial.write("$$$P" + str(offset + 6) + ",6,ON\r")
    serial.write("$$$P" + str(offset + 6) + ",7,ON\r")
    serial.write("$$$P" + str(offset + 6) + ",8,ON\r")
    serial.write("$$$P" + str(offset + 6) + ",9,ON\r")
    return


def six(offset):
    serial.write("$$$P" + str(offset + 2) + ",1,ON\r")
    serial.write("$$$P" + str(offset + 2) + ",2,ON\r")
    serial.write("$$$P" + str(offset + 2) + ",3,ON\r")
    serial.write("$$$P" + str(offset + 2) + ",4,ON\r")
    serial.write("$$$P" + str(offset + 2) + ",5,ON\r")
    serial.write("$$$P" + str(offset + 2) + ",6,ON\r")
    serial.write("$$$P" + str(offset + 2) + ",7,ON\r")
    serial.write("$$$P" + str(offset + 2) + ",8,ON\r")
    serial.write("$$$P" + str(offset + 2) + ",9,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",1,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",2,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",3,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",4,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",5,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",6,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",7,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",8,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",9,ON\r")
    serial.write("$$$P" + str(offset + 4) + ",1,ON\r")
    serial.write("$$$P" + str(offset + 4) + ",5,ON\r")
    serial.write("$$$P" + str(offset + 4) + ",9,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",1,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",5,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",6,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",7,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",8,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",9,ON\r")
    serial.write("$$$P" + str(offset + 6) + ",1,ON\r")
    serial.write("$$$P" + str(offset + 6) + ",2,ON\r")
    serial.write("$$$P" + str(offset + 6) + ",5,ON\r")
    serial.write("$$$P" + str(offset + 6) + ",6,ON\r")
    serial.write("$$$P" + str(offset + 6) + ",7,ON\r")
    serial.write("$$$P" + str(offset + 6) + ",8,ON\r")
    serial.write("$$$P" + str(offset + 6) + ",9,ON\r")
    return


def seven(offset):
    serial.write("$$$P" + str(offset + 2) + ",1,ON\r")
    serial.write("$$$P" + str(offset + 2) + ",2,ON\r")
    serial.write("$$$P" + str(offset + 2) + ",3,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",1,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",2,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",3,ON\r")
    serial.write("$$$P" + str(offset + 4) + ",1,ON\r")
    serial.write("$$$P" + str(offset + 4) + ",2,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",1,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",2,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",3,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",4,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",5,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",6,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",7,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",8,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",9,ON\r")
    serial.write("$$$P" + str(offset + 6) + ",1,ON\r")
    serial.write("$$$P" + str(offset + 6) + ",2,ON\r")
    serial.write("$$$P" + str(offset + 6) + ",3,ON\r")
    serial.write("$$$P" + str(offset + 6) + ",4,ON\r")
    serial.write("$$$P" + str(offset + 6) + ",5,ON\r")
    serial.write("$$$P" + str(offset + 6) + ",6,ON\r")
    serial.write("$$$P" + str(offset + 6) + ",7,ON\r")
    serial.write("$$$P" + str(offset + 6) + ",8,ON\r")
    serial.write("$$$P" + str(offset + 6) + ",9,ON\r")
    return


def eight(offset):
    serial.write("$$$P" + str(offset + 2) + ",2,ON\r")
    serial.write("$$$P" + str(offset + 2) + ",3,ON\r")
    serial.write("$$$P" + str(offset + 2) + ",4,ON\r")
    serial.write("$$$P" + str(offset + 2) + ",6,ON\r")
    serial.write("$$$P" + str(offset + 2) + ",7,ON\r")
    serial.write("$$$P" + str(offset + 2) + ",8,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",1,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",2,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",3,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",4,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",5,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",6,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",7,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",8,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",9,ON\r")
    serial.write("$$$P" + str(offset + 4) + ",1,ON\r")
    serial.write("$$$P" + str(offset + 4) + ",5,ON\r")
    serial.write("$$$P" + str(offset + 4) + ",9,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",1,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",2,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",3,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",4,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",5,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",6,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",7,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",8,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",9,ON\r")
    serial.write("$$$P" + str(offset + 6) + ",2,ON\r")
    serial.write("$$$P" + str(offset + 6) + ",3,ON\r")
    serial.write("$$$P" + str(offset + 6) + ",4,ON\r")
    serial.write("$$$P" + str(offset + 6) + ",6,ON\r")
    serial.write("$$$P" + str(offset + 6) + ",7,ON\r")
    serial.write("$$$P" + str(offset + 6) + ",8,ON\r")
    return


def nine(offset):
    serial.write("$$$P" + str(offset + 2) + ",2,ON\r")
    serial.write("$$$P" + str(offset + 2) + ",3,ON\r")
    serial.write("$$$P" + str(offset + 2) + ",4,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",1,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",2,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",3,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",4,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",5,ON\r")
    serial.write("$$$P" + str(offset + 3) + ",9,ON\r")
    serial.write("$$$P" + str(offset + 4) + ",1,ON\r")
    serial.write("$$$P" + str(offset + 4) + ",5,ON\r")
    serial.write("$$$P" + str(offset + 4) + ",9,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",1,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",2,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",3,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",4,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",5,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",6,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",7,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",8,ON\r")
    serial.write("$$$P" + str(offset + 5) + ",9,ON\r")
    serial.write("$$$P" + str(offset + 6) + ",2,ON\r")
    serial.write("$$$P" + str(offset + 6) + ",3,ON\r")
    serial.write("$$$P" + str(offset + 6) + ",4,ON\r")
    serial.write("$$$P" + str(offset + 6) + ",6,ON\r")
    serial.write("$$$P" + str(offset + 6) + ",7,ON\r")
    serial.write("$$$P" + str(offset + 6) + ",8,ON\r")
    return


def get_cpu_load():
    return psutil.cpu_percent(interval=1)


# function skips redraw when idle
def should_redraw(load):
    digits = str(load).split(".")[0]
    if len(digits) > 1:
        return True
    elif int(digits[0]) > idle_threshold:
        return True
    else:
        return False


def display_load(percentage):
    digits = str(percentage).split(".")[0]  # truncate at floating point
    if len(digits) == 3:  # display 99% when load at 100%
        digit1 = 9
        digit2 = 9
    elif len(digits) == 2:
        digit1 = int(digits[0])
        digit2 = int(digits[1])
    else:
        digit1 = 0
        digit2 = int(digits[0])
    if digit1 == 0:
        zero(tens_offset)
    elif digit1 == 1:
        one(tens_offset)
    elif digit1 == 2:
        two(tens_offset)
    elif digit1 == 3:
        three(tens_offset)
    elif digit1 == 4:
        four(tens_offset)
    elif digit1 == 5:
        five(tens_offset)
    elif digit1 == 6:
        six(tens_offset)
    elif digit1 == 7:
        seven(tens_offset)
    elif digit1 == 8:
        eight(tens_offset)
    elif digit1 == 9:
        nine(tens_offset)
    if digit2 == 0:
        zero(ones_offset)
    elif digit2 == 1:
        one(ones_offset)
    elif digit2 == 2:
        two(ones_offset)
    elif digit2 == 3:
        three(ones_offset)
    elif digit2 == 4:
        four(ones_offset)
    elif digit2 == 5:
        five(ones_offset)
    elif digit2 == 6:
        six(ones_offset)
    elif digit2 == 7:
        seven(ones_offset)
    elif digit2 == 8:
        eight(ones_offset)
    if digit2 == 9:
        nine(ones_offset)

init()
splash()
while True:
    load = get_cpu_load()
    if should_redraw(load):
        display_load(load)
    else:
        serial.write(idle_text[randint(0, 9)])
        time.sleep(2)
    time.sleep(2)
    all_leds_off()

