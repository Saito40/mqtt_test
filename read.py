"""

"""
from RPi import GPIO  # pylint: disable=E0401
import random

from subscriber import Subscriber
from key_reader import KeyReader, KeyReader2
import setting

client_press_id = f'python-mqtt-{random.randint(0, 1000)}'
client_release_id = f'python-mqtt-{random.randint(0, 1000)}'
running = True

if __name__ == '__main__':
    press_subscriber = Subscriber(
        client_press_id,
        setting.BROKER,
        setting.PORT)
    release_subscriber = Subscriber(
        client_release_id,
        setting.BROKER,
        setting.PORT)
    press_subscriber.loop_start()
    release_subscriber.loop_start()

    l_fw = KeyReader(setting.L_FW)
    l_back = KeyReader(setting.L_BACK)
    r_fw = KeyReader(setting.R_FW)
    r_back = KeyReader(setting.R_BACK)
    at_l = KeyReader(setting.AT_L)
    at_r = KeyReader(setting.AT_R)
    at_up = KeyReader(setting.AT_UP)
    at_down = KeyReader(setting.AT_DOWN)
    at_set = KeyReader2(setting.AT_SET, setting.AT_SET["check_pin"])
    camera_l = KeyReader(setting.CAMERA_L)
    camera_r = KeyReader(setting.CAMERA_R)
    camera_init = KeyReader(setting.CAMERA_INIT)

    def press(msg):
        global running
        l_fw.press(msg)
        l_back.press(msg)
        r_fw.press(msg)
        r_back.press(msg)
        at_l.press(msg)
        at_r.press(msg)
        at_up.press(msg)
        at_down.press(msg)
        at_set.press(msg)
        camera_l.press(msg)
        camera_r.press(msg)
        camera_init.press(msg)
        if msg == "ESCAPE":
            running = False

    def release(msg):
        l_fw.release(msg)
        l_back.release(msg)
        r_fw.release(msg)
        r_back.release(msg)
        at_l.release(msg)
        at_r.release(msg)
        at_up.release(msg)
        at_down.release(msg)
        at_set.release(msg)
        camera_l.release(msg)
        camera_r.release(msg)
        camera_init.release(msg)

    press_subscriber.client.subscribe(setting.PRESS_TOPIC, press)
    press_subscriber.client.subscribe(setting.RELEASE_TOPIC, release)

    while running:
        pass

    GPIO.cleanup()
