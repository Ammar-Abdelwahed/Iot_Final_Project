#pi_Subscriber.py
import paho.mqtt.client as mqtt
import ssl 
from time import sleep
import serial
import subprocess 
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    topics = ["speed_car","directions"] # Subscribed Topics
    for topic in topics : 
        client.subscribe(topic)
    print("Subscribed on:",topics) 
    
def Get_KeyboardPress_Script() :
    global keyboardProcess
    keyboardProcess = subprocess.Popen(["python","keyboard_monitor.py"],bufsize=0)
    print(keyboardProcess)


def on_message(client, userdata, msg):  # The callback function -> it will be triggered when receiving messages
    print(f"{msg.topic}:{str(msg.payload)}") #get msg in bytes 
    if msg.payload == b"open keyboard" :
        Get_KeyboardPress_Script() 
    elif msg.payload == b"close keyboard" :
        keyboardProcess.terminate()
    #ser.write(msg.payload)

if __name__ == "__main__" :
    client = mqtt.Client(client_id="20")
    client.username_pw_set("Server","Server123") # User Credentials for Broker 
    client.tls_set(ca_certs=None, certfile=None, keyfile=None, cert_reqs=ssl.CERT_NONE, tls_version=ssl.PROTOCOL_TLSv1_2) #Tls Authentication 
    client.on_connect = on_connect
    client.on_message = on_message
    ser = serial.Serial('/dev/ttyS0', 9600, timeout=1)
    ser.reset_input_buffer()
    client.connect("", 8883, 60)
    client.loop_forever()    
    




