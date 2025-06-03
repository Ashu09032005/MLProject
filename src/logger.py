import logging
import os
from datetime import datetime

# Step 1: Define log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Step 2: Ensure logs folder exists
#Gets the current working directory where your Python script is running (e.g., "C:/Users/Lenovo/Desktop/MLProject").
logs_path = os.path.join(os.getcwd(), "logs")
#Prevents an error if the folder already exists.
os.makedirs(logs_path, exist_ok=True)

# Step 3: Full path to the log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Step 4: Configure logging
# The level of the message (INFO, ERROR, etc.).
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(levelname)s - %(message)s",
    level=logging.INFO
)

# Step 5: Write a test log message
if __name__ == "__main__":
    logging.info("✅ Logging has started successfully")
    print(f"Log written to: {LOG_FILE_PATH}")
