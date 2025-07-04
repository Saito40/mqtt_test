from gpiozero import AngularServo
from gpiozero.pins.pigpio import PiGPIOFactory
import threading
import time

import setting

sleep_step = 0.1


class ServoControl:
    N = "N"
    L = "L"
    R = "R"

    def __init__(self, key_l, key_r, key_init, pin):
        self.key_l = key_l
        self.key_r = key_r
        self.key_init = key_init
        self.pin = pin
        self.status = ServoControl.N
        factory = PiGPIOFactory()
        self.a_servo = AngularServo(
            pin,
            min_angle=setting.C_SERVO["min_deg"],
            max_angle=setting.C_SERVO["max_deg"],
            min_pulse_width=0.5/1000,
            max_pulse_width=2.4/1000,
            frame_width=1/50,
            pin_factory=factory)
        self.a_servo.angle = setting.C_SERVO["init_deg"]
        # self.to_angle = setting.C_SERVO["init_deg"]
        self.thread = threading.Thread(target=self.loop)
        self.count = 0
        self.run = True
        self.thread.daemon = False
        self.thread.start()

    def run_init(self, try_key):
        if self.key_init != try_key:
            return
        if self.status != ServoControl.N:
            print("pressed other")
            return
        self.a_servo.angle = setting.C_SERVO["init_deg"]
        # self.to_angle = setting.C_SERVO["init_deg"]

    def run_left(self, try_key):
        if self.key_l != try_key:
            return
        if self.status == ServoControl.R:
            self.status = ServoControl.N
        else:
            self.status = ServoControl.L

    def run_right(self, try_key):
        if self.key_r != try_key:
            return
        if self.status == ServoControl.L:
            self.status = ServoControl.N
        else:
            self.status = ServoControl.R

    def stop_left(self, try_key):
        if self.key_init != try_key:
            return
        if self.status == ServoControl.N:
            self.status = ServoControl.R
        else:
            self.status = ServoControl.N

    def stop_right(self, try_key):
        if self.key_r != try_key:
            return
        if self.status == ServoControl.N:
            self.status = ServoControl.L
        else:
            self.status = ServoControl.N

    def loop(self):
        while self.run:
            if self.status == ServoControl.L:
                self.a_servo.angle = min(
                    setting.C_SERVO["max_deg"],
                    self.a_servo.angle + setting.C_SERVO["step_deg"]
                )
            elif self.status == ServoControl.R:
                self.a_servo.angle = max(
                    setting.C_SERVO["min_deg"],
                    self.a_servo.angle - setting.C_SERVO["step_deg"]
                )
            else:
                # self.status == ServoControl.N
                pass
            if self.count % 10 == 0:
                print(self.a_servo.angle)
            time.sleep(sleep_step)

    def cleanup(self):
        self.run = False
