import json
from datetime import datetime

def log_data(data):
    with open("logs.txt", "a") as f:
        f.write(json.dumps({
            "timestamp": str(datetime.now()),
            **data
        }) + "\n")