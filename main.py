import os
from datetime import datetime, timezone

os.makedirs("data", exist_ok=True)
now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")

with open("data/log.md", "a") as f:
    for i in range(1, 6):
        line = f"- [{now} UTC] Line {i}"
        print(line)
        f.write(line + "\n")
