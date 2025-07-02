# python 3.6 https://qiita.com/emqx_japan/items/b63c918fe137a6db4b37

import random
import time
import pygame
import sys

from paho.mqtt import client as mqtt_client

import setting

test_topic = "python/mqtt"
client_id = f'python-mqtt-{random.randint(0, 1000)}'


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(setting.BROKER, setting.PORT)
    return client


def publish(client, topic, msg):
    result = client.publish(topic, msg, 1)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        print(f"Send `{msg}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")


def publish_test(client):
    msg_count = 0
    while True:
        time.sleep(1)
        msg = f"messages: {msg_count}"
        result = client.publish(test_topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{test_topic}`")
        else:
            print(f"Failed to send message to topic {test_topic}")
        msg_count += 1


def run_pygame(client):
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
                key_name = pygame.key.name(event.key)
                pressed.add(key_name)
                publish(client, setting.PRESS_TOPIC, event.key)
                if event.key == setting.AT_SET["key"]:
                    publish(client, setting.AT_SET_TOPIC, event.key)
                change_key = True

            elif event.type == pygame.KEYUP:
                key_name = pygame.key.name(event.key)
                pressed.discard(key_name)
                publish(client, setting.RELEASE_TOPIC, event.key)
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
    client = connect_mqtt()
    client.loop_start()
    # publish_test(client)
    run_pygame(client)
