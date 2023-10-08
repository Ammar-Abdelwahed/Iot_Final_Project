import paho.mqtt.client as mqtt
import time
import ssl
import Adafruit_DHT
import random
# Define the MQTT broker's address and port
broker_address = "9f546752e5564dcaae715934de954a6f.s2.eu.hivemq.cloud" #broker address 
broker_port = 8883

# Create an MQTT client instance
client = mqtt.Client("RaspberryPiPublisher")

# Connect to the broker
client.connect(broker_address, broker_port)
client.username_pw_set("omar2033","Panzer123") # User Credentials for Broker 
client.tls_set(ca_certs=None, certfile=None, keyfile=None, cert_reqs=ssl.CERT_NONE, tls_version=ssl.PROTOCOL_TLSv1_2) #Tls Authentication 
client.connect(broker_address, broker_port)    
print("Connected on Broker !")
sensor=Adafruit_DHT.DHT11 
gpio=17
print("DHT_initalized")
while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
    else:
        print('Failed to get reading. Try again!')

    # Publish a message to a topic
    temp_topic = "temperature"
    humd_topic = "humidity"    
    client.publish(temp_topic, temperature)
    client.publish(humd_topic, humidity)
    print(f"Published: {temperature} to topic: {temp_topic}")
    print(f"Published: {humidity} to topic: {humd_topic}")
    time.sleep(2)  

#if you want to disconnect 
client.disconnect()