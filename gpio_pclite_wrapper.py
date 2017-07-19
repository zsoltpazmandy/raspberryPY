import time
import sys
import serial
import numpy

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


# function to feed and display data, where pattern data is 126 bits
def map_to_display(pattern):
    pattern = stringify(mirror_hor(rotate_cw(pattern)))
    param = "$$$F" + pattern + "\r"
    serial.write(param)


# function to rotate the matrix clock-wise
def rotate_cw(pattern):
    return zip(*pattern[::-1])


# function to mirror pattern horizontally
def mirror_hor(input_pattern):
    return numpy.fliplr(input_pattern)


# function to concatenate and
def stringify(matrix):
    string = ""
    for row in matrix:
        string += str(row)\
            .replace("[", "")\
            .replace("]", "")\
            .replace(",", "")\
            .replace(" ", "")\
            .replace("(", "")\
            .replace(")", "")\
            .replace("'", "")
    return string


test_pattern = ['01111111111111',
                '01111111111111',
                '00000000001110',
                '00000000111000',
                '00000011100000',
                '00001110000000',
                '00111000000000',
                '01111111111111',
                '01111111111111']

if len(sys.argv) != 2:
    print "Invalid number of arguments: " + str(len(sys.argv))
         
else:
    init()
    flash_screen()
    map_to_display(sys.argv[1])

