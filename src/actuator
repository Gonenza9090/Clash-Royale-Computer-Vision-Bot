import random
import time
from ppadb.client import Client as AdbClient

# These are card coordinate where this code picks the card, the deployment was test on Bluestack emulator to run the game, so these coodinates may change depending on your game host
sl1 = (290, 1430) 
sl2 = (450, 1430)
sl3 = (610, 1430)
sl4 = (770, 1430)

slots = [sl1, sl2, sl3, sl4] # This randomly selects a card to deploy
select_radius = 15 # This is the radius around the centre of cards, this makes sure everytime selects card from a different co-ordinates to disguise the Clashe Royale bot detector

delay_range = [0.5, 1.5] # Time interval between card selection and its deployment on arean, this time duration mimics the human like card picking and holding before deployment

bridges_co = [(215,730), (682,730)] # These are the coordinates of tiles of both sides of bridges which are just below
arean_radius = 10 # Same logic as select_radius

def connect():
    # 1. Connect to the ADB Server (the middleman)
    client = AdbClient(host="127.0.0.1", port=5037)
    
    # 2. Get a list of ALL connected devices
    devices = client.devices()
    
    if len(devices) == 0:
        print("BlueStacks not found! Is ADB toggled ON in settings?")
        return None
    
    # 3. Just take the first one that is active
    device = devices[0]
    print(f"Connected to: {device.serial}")
    return device

def play_card(device):
    # Simulate a human: Click the card everytime on different coordinates within the card area, then drop the card on arena with a deliberate time lack

    select = random.choice([sl1, sl2, sl3, sl4]) # Selects card randomly
    
    # This selects a coordinate within card of radius 15 pixels and everytime that coordinates changes 
    x_diff = random.randint(-select_radius, select_radius) 
    y_diff = random.randint(-select_radius, select_radius)
    device.shell(f"input tap {select[0] + x_diff} {select[1] + y_diff}")
    
    # Tiny delay 
    delay = random.uniform(delay_range[0], delay_range[1])
    time.sleep(delay)
    
    # Drop it in the arena 
    select1 = random.choice(bridges_co)
    x_diff1 = random.randint(-arean_radius, arean_radius)
    y_diff1 = random.randint(-arean_radius, arean_radius)
    device.shell(f"input tap {select1[0] + x_diff1} {select1[1] + y_diff}")



bluestacks = connect()

if bluestacks:
    print("Connected! Bot is LIVE. Press Ctrl+C to STOP.")
    try:
        while True:
            play_card(bluestacks)
            
            wait_time = random.uniform(3, 10) # Random wait between deployments

            print(f"Waiting {wait_time:.2f}s for next move...")
            time.sleep(wait_time)

    except KeyboardInterrupt:
        print("\n[!] Emergency Stop Triggered. Bot is shutting down.")
