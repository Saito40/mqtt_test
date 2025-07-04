"""

"""
from datetime import datetime

import setting


class EmergencyStop:
    def __init__(self):
        self.times = [datetime(0)] * setting.EMERGENCY_COUNT
        self.running = True

    def check(self):
        if not self.running:
            return
        self.times.append(datetime.now())
        self.times.pop(0)
        delta = self.times[-1] - self.times[0]
        running = delta < setting.EMERGENCY_SPAN
        if not running:
            print("Emergency Stop")
        self.running = running
