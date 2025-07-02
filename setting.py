import pygame

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

CAMERA_L    = {"key": pygame.K_LEFT , "pin": 22}
CAMERA_R    = {"key": pygame.K_RIGHT, "pin": 27}
CAMERA_INIT = {"key": pygame.K_DOWN , "pin": 17}

AT_SET_OK_PIN = 0

PRESS_TOPIC = "test/pressed"
RELEASE_TOPIC = "test/released"
