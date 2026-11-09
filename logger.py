import logging
import sys
from pathlib import Path

# Configure global logging for automation-tool-12
def setup_logger(name: str = 'autoclicker', log_file: str = 'app.log') -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # File handler
    log_path = Path(log_file)
    file_handler = logging.FileHandler(log_path)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    return logger

# Singleton instance for application-wide use
logger = setup_logger()