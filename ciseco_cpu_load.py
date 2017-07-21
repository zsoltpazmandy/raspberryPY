import psutil
import time
import sys
import serial

serial = serial.Serial()
serial.baudrate = 9600
serial.timeout = 0
serial.port = "/dev/serial0"


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


# function to flash all LEDs on the display
def flash_screen():
    all_leds_on()
    time.sleep(0.1)
    all_leds_off()


def get_cpu_load():
    return psutil.cpu_percent(interval=1)


def display_load(load):
    load = str(load).replace(",", "")
    serial.write("$$$B1," + load + "\r")
    serial.write("$$$B2," + load + "\r")
    serial.write("$$$B3," + load + "\r")
    serial.write("$$$B4," + load + "\r")
    serial.write("$$$B5," + load + "\r")
    serial.write("$$$B6," + load + "\r")
    serial.write("$$$B7," + load + "\r")
    serial.write("$$$B8," + load + "\r")
    serial.write("$$$B9," + load + "\r")
    serial.write("$$$B10," + load + "\r")
    serial.write("$$$B11," + load + "\r")
    serial.write("$$$B12," + load + "\r")
    serial.write("$$$B13," + load + "\r")
    serial.write("$$$B14," + load + "\r")

init()
flash_screen()
while True:
    display_load(get_cpu_load())
    time.sleep(0.1);