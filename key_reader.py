"""

"""
import time
from RPi import GPIO  # pylint: disable=E0401
# from gpiozero import Button  # pylint: disable=E0401
# from gpiozero.pins.pigpio import PiGPIOFactory  # pylint: disable=E0401

GPIO.setmode(GPIO.BCM)


class KeyReader:
    def __init__(self, key_pin):
        self.key = key_pin["key"]
        self.pin = key_pin["pin"]
        GPIO.setup(self.pin, GPIO.OUT)

    def press(self, try_key):
        if try_key != self.key:
            return
        GPIO.output(self.pin, True)

    def release(self, try_key):
        if try_key != self.key:
            return
        GPIO.output(self.pin, False)


class KeyReader2:
    def __init__(self, key_pin, check_pin):
        self.key = key_pin["key"]
        self.pin = key_pin["pin"]
        GPIO.setup(self.pin, GPIO.OUT)
        self.check_pin = check_pin
        GPIO.setup(check_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        self.running = False

    def press(self, try_key):
        if try_key != self.key:
            return
        GPIO.output(self.pin, True)
        while GPIO.input(self.check_pin) == GPIO.LOW:
            time.sleep(0.1)
        GPIO.output(self.pin, False)

    def release(self, try_key):
        pass
