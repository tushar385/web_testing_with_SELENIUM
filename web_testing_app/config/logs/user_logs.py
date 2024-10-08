import os

LOG_FILE = os.path.join(os.path.dirname(__file__), "user_logs.txt")

def clear_logs():
    with open(LOG_FILE, "w") as f:
        f.write("") 

def log_message(message):
    with open(LOG_FILE, "a") as f:
        f.write(message + "\n")

def read_logs():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            return f.readlines()
    return []
