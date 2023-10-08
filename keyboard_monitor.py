from pynput.keyboard import Key, Listener

# Define a callback function to handle key events
message = b'S'
def on_key_press(key):
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
        elif (key.char == 'l') :
            message =b"1"
        if message in [b'B',b'L',b'L',]           
    except Exception as e:
        print(f"Error: {str(e)}")

def on_key_release(key):
    #if key != key and key != key.m  and key != key.l :
    message = b"S"

# Create a listener that monitors keyboard events
# Define the MQTT broker's address and port
broker_address = "9f546752e5564dcaae715934de954a6f.s2.eu.hivemq.cloud" #broker address 
broker_port = 8883

# Create an MQTT client instance
client = mqtt.Client("RaspberryPiPublisher")

# Connect to the broker
client.connect(broker_address, broker_port)

with Listener(on_press=on_key_press, on_release=on_key_release) as listener:
    listener.join()