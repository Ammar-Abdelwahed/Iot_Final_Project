from pynput.keyboard import Key, Listener
import paho.mqtt.client as mqtt
import ssl
# Define a callback function to handle key events
message = b'S'
lastmessage =b'S'
def on_key_press(key):
    global message , lastmessage 
    try:
        # You can add your custom logic here to process the key press event
        if (key == Key.up) :
            message =b"F"
        elif (key == Key.down) :
            message=b"B"
        elif  (key == Key.right) :
            message =b"R"
        elif (key == Key.left) :
            message = b"L" 
        elif (key.char == 'q') :
            message =b"q" 
        elif (key.char == 'm') :    
            message =b"5"
        elif (key.char == 'o') :
            message = b"O"
        elif (key.char == 'c') :
            message = b"C"
        elif (key.char == 'l') :
            message =b"1"
        else :
            pass      
        if (message in [b'B',b'L',b'R',b'F',b'O',b'C'] ) and (message != lastmessage):
            topic = "directions"   
            client.publish(topic,payload =message)
            print(f"Published: {message} to topic: {topic}")
            lastmessage = message 
        else :
            if message != lastmessage :
                topic = "speed_car"   
                client.publish(topic, message)
                print(f"Published: {message} to topic: {topic}")
                lastmessage = message 


    except Exception as e:
        print(f"Error: {str(e)}")

def on_key_release(key):
    global message , lastmessage 
    if message in [b'B',b'L',b'R',b'F'] :
            topic = "directions"   
            message = b"S"
            lastmessage = b"S"
            client.publish(topic, message)
            print(f"Published: {message} to topic: {topic}")
# Create a listener that monitors keyboard events
# Define the MQTT broker's address and port
broker_address = "9f546752e5564dcaae715934de954a6f.s2.eu.hivemq.cloud" #broker address 
broker_port = 8883

# Create an MQTT client instance
client = mqtt.Client("KeyboardPublisher")

# Connect to the broker
client.username_pw_set("omar2033","Panzer123") # User Credentials for Broker 
client.tls_set(ca_certs=None, certfile=None, keyfile=None, cert_reqs=ssl.CERT_NONE, tls_version=ssl.PROTOCOL_TLSv1_2) #Tls Authentication 
client.connect(broker_address, broker_port)    
print("Connected on Broker !")
with Listener(on_press=on_key_press, on_release=on_key_release) as listener:
    listener.join(client.loop_forever())