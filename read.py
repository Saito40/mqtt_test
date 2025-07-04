"""

"""
from RPi import GPIO  # pylint: disable=E0401
import random

camera_s = None
try:
    from control.subscriber import Subscriber
    from control.key_reader import KeyReader, KeyReader2
    from control.emergency_stop import EmergencyStop
    from control.servo_control import ServoControl
    import setting

    client_press_id = f'python-mqtt-{random.randint(0, 1000)}'
    client_release_id = f'python-mqtt-{random.randint(0, 1000)}'
    client_at_set_id = f'python-mqtt-{random.randint(0, 1000)}'
    # running = True
    e_stop = EmergencyStop()

    if __name__ == '__main__':
        press_subscriber = Subscriber(
            client_press_id,
            setting.BROKER,
            setting.PORT)
        release_subscriber = Subscriber(
            client_release_id,
            setting.BROKER,
            setting.PORT)
        at_set_subscriber = Subscriber(
            client_at_set_id,
            setting.BROKER,
            setting.PORT)
        press_subscriber.client.loop_start()
        release_subscriber.client.loop_start()
        at_set_subscriber.client.loop_start()

        l_fw = KeyReader(setting.L_FW)
        l_back = KeyReader(setting.L_BACK)
        r_fw = KeyReader(setting.R_FW)
        r_back = KeyReader(setting.R_BACK)
        at_l = KeyReader(setting.AT_L)
        at_r = KeyReader(setting.AT_R)
        at_up = KeyReader(setting.AT_UP)
        at_down = KeyReader(setting.AT_DOWN)
        at_set = KeyReader2(setting.AT_SET, setting.AT_SET["check_pin"])

        camera_s = ServoControl(
            setting.CAMERA["key_l"],
            setting.CAMERA["key_r"],
            setting.CAMERA["key_init"],
            setting.CAMERA["pin"])

        def press(msg):
            # global running
            l_fw.press(msg)
            l_back.press(msg)
            r_fw.press(msg)
            r_back.press(msg)
            at_l.press(msg)
            at_r.press(msg)
            at_up.press(msg)
            at_down.press(msg)
            camera_s.run_left(msg)
            camera_s.run_right(msg)
            camera_s.run_init(msg)
            if msg == str(setting.EMERGENCY_KEY):
                e_stop.check()

        def release(msg):
            l_fw.release(msg)
            l_back.release(msg)
            r_fw.release(msg)
            r_back.release(msg)
            at_l.release(msg)
            at_r.release(msg)
            at_up.release(msg)
            at_down.release(msg)
            camera_s.stop_left(msg)
            camera_s.stop_right(msg)

        def at_set_func(msg):
            at_set.press(msg)

        press_subscriber.subscribe(setting.PRESS_TOPIC, press)
        release_subscriber.subscribe(setting.RELEASE_TOPIC, release)
        at_set_subscriber.subscribe(setting.AT_SET_TOPIC, at_set_func)
        # while running:
        while e_stop.running:
            pass
except Exception as ex:
    print(ex)
    pass

if camera_s:
    camera_s.cleanup()
GPIO.cleanup()
print("CLEANUP")
