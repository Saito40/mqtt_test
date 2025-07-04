"""

"""
from paho.mqtt import client as mqtt_client


class Subscriber:
    def __init__(self, client_id, broker, port):
        self.client = mqtt_client.Client(
            client_id=client_id,
            callback_api_version=mqtt_client.CallbackAPIVersion.VERSION2)
        self.client.on_connect = Subscriber.on_connect
        self.client.connect(broker, port)

    def subscribe(self, topic, func):
        def on_message(client, userdata, msg):
            decoded = msg.payload.decode()
            print(f"Received `{decoded}` from `{msg.topic}` topic")
            func(decoded)

        self.client.subscribe(topic, 1)
        self.client.on_message = on_message

    @staticmethod
    def on_connect(client, userdata, flags, rc, properties=None):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
