import paho.mqtt.client as mqtt
import datetime
import time

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
    else:
        print(f"Connection failed with code {rc}")

broker_address = 'broker.emqx.io'
client = mqtt.Client()
client.on_connect = on_connect
client.connect(broker_address, port=1883, keepalive=60) #alive for 60 min
client.loop_start()


topic = "/device/EO1"
current_time = datetime.datetime.now()
payload = {
	"did":EO1,
	"temperature":37
	"timestamp":current_time
	}

for _ in range(360):  # 60 minutes * 6(10-seconds)
    client.publish(topic, payload)
    time.sleep(10)

client.disconnect()