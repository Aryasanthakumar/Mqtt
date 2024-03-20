import paho.mqtt.client as mqtt
import datetime
import csv

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
        client.subscribe("/device/")
    else:
        print(f"Connection failed with code {rc}")

def on_message(client, userdata, msg):
    userdata["message_count"] += 1


start_time = datetime.datetime.now()
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

broker_address = "mqtt.broker.com"
client.connect(broker_address, port=1883)

client.loop_start()

# Run for 60 minutes (60 *60)
client.loop(timeout=3600)

end_time = datetime.datetime.now()
latency = start_time - end_time
maximum = max(latency)
minimum = min(latency)
avg = (maximum + minimum)/2
count = client.user_data_get()['message_count']
report_data = [latency, maximum, minimum, avg, count]

with open('report.csv', 'w', newline='') as csvfile:
    rep_writer = csv.writer(csvfile)
    rep_writer.writerow(report_data)

client.disconnect()
