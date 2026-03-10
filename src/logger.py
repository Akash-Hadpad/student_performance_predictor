import logging 
import os
from datetime import datetime
LOG_FILE=f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log "
logs_path=os.path.join(os.getcwd(),'logs',LOG_FILE)
os.makedirs(logs_path,exist_ok=True)
logging.basicConfig(
    filename=LOG_FILE,
    format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)    
if __name__ == "__main__":
    logging.info("Logging setup complete. Logs will be saved to: %s", logs_path)
