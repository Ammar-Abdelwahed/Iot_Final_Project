import paho.mqtt.client as mqtt
import time

# Define the MQTT broker's address and port
broker_address = "" #broker address 
broker_port = 8883

# Create an MQTT client instance
client = mqtt.Client("RaspberryPiPublisher")

# Connect to the broker
client.connect(broker_address, broker_port)

while True:
    # Publish a message to a topic
    topic = "your/topic"  
    message = "Hello, MQTT!"  
    client.publish(topic, message)
    print(f"Published: {message} to topic: {topic}")
    time.sleep(5)  

#if you want to disconnect 
client.disconnect()