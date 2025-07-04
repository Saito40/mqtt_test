"""

"""
from datetime import datetime

import setting


class EmergencyStop:
    def __init__(self):
        self.times = [datetime.now()] * setting.EMERGENCY_COUNT
        self.running = True

    def check(self):
        if not self.running:
            return
        self.times.append(datetime.now())
        self.times.pop(0)
        delta = self.times[-1] - self.times[0]
        print(delta.seconds)
        running = setting.EMERGENCY_SPAN < delta.seconds
        if not running:
            print("Emergency Stop")
        self.running = running
