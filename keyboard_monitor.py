from pynput.keyboard import Key, Listener

# Define a callback function to handle key events
def on_key_press(key):
    try:
        # You can add your custom logic here to process the key press event
        if (key == Key.up) :
            print(b"F")
        elif (key == Key.down) :
            print(b"B")
        elif  (key == Key.right) :
            print(b"R")
        elif (key == Key.left) :
            print(b"L") 
        elif (key.char == 'q') :
            print(b"q") 
        elif (key.char == 'm') :
            print(b"5")
        elif (key.char == 'l') :
            print(b"1")       
    except Exception as e:
        print(f"Error: {str(e)}")

def on_key_release(key):
    #if key != key and key != key.m  and key != key.l :
    print("S")

# Create a listener that monitors keyboard events
with Listener(on_press=on_key_press, on_release=on_key_release) as listener:
    listener.join()