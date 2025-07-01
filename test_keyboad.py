# python 3.6 https://qiita.com/emqx_japan/items/b63c918fe137a6db4b37

# import random
# import time
import pygame
import sys

import setting


def run_pygame():
    # 初期化
    pygame.init()
    WIDTH, HEIGHT = 640, 480
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pressed Keys Display")

    font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()
    FPS = 60

    pressed = set()
    running = True
    change_key = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                for data in [
                                setting.L_FW, setting.L_BACK, setting.R_FW,
                                setting.R_BACK, setting.AT_L, setting.AT_R,
                                setting.AT_UP, setting.AT_DOWN, setting.AT_SET,
                                setting.CAMERA_L, setting.CAMERA_R,
                                setting.CAMERA_INIT,]:
                    if data["key"] == event.key:
                        print("OK", pygame.key.name(data["key"]), data["pin"])
                        break
                else:
                    print("unknown", pygame.key.name(event.key), event.key)

                key_name = pygame.key.name(event.key)
                pressed.add(key_name)
                change_key = True

            elif event.type == pygame.KEYUP:
                key_name = pygame.key.name(event.key)
                pressed.discard(key_name)
                change_key = True

        # 表示更新するか判定
        if change_key:
            screen.fill((30, 30, 30))
            if pressed:
                sorted_key = sorted(pressed)
                join_key = ", ".join(sorted_key)
                text = "Pressed: " + join_key
            else:
                text = "Pressed: None"
            img = font.render(text, True, (255, 255, 255))
            screen.blit(img, (20, HEIGHT // 2 - 20))
            pygame.display.flip()
        change_key = False
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    run_pygame()
