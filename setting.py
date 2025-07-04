import pygame
from datetime import timedelta

BROKER = '192.168.11.8'
PORT = 1883

L_FW   = {"key": pygame.K_w     , "pin": 26}
L_BACK = {"key": pygame.K_z     , "pin": 19}
R_FW   = {"key": pygame.K_AT    , "pin": 13}
R_BACK = {"key": pygame.K_PERIOD, "pin":  6}

AT_L    = {"key": pygame.K_KP6, "pin": 21}
AT_R    = {"key": pygame.K_KP4, "pin": 20}
AT_UP   = {"key": pygame.K_KP8, "pin": 16}
AT_DOWN = {"key": pygame.K_KP2, "pin": 12}
AT_SET  = {"key": pygame.K_KP0, "pin": 24, "check_pin": 23}

# 12, 13, 18, 19
# 12 = 18, 13 = 19
CAMERA = {
    "key_l": pygame.K_LEFT,
    "key_r": pygame.K_RIGHT,
    "key_init": pygame.K_DOWN,
    "pin": 18
}

AT_SET_OK_PIN = 0

C_SERVO = {
    "min_deg": -90.,
    "max_deg": 90.,
    "init_deg": 0.,
    "step_deg": 5
}

PRESS_TOPIC = "test/pressed"
RELEASE_TOPIC = "test/released"
AT_SET_TOPIC = "test/at_set"

EMERGENCY_COUNT = 3
EMERGENCY_SPAN = 1
EMERGENCY_KEY = pygame.K_ESCAPE
