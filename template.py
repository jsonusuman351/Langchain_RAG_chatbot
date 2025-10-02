import os
from pathlib import Path
import logging

# Basic logging configuration
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# List of all files and folders (excluding .docx and .pdf files)
list_of_files = [
    ".env",
    "api/app.log",
    "api/chroma_utils.py",
    "api/db_utils.py",
    "api/langchain_utils.py",
    "api/main.py",
    "api/pydantic_models.py",
    "api/requirements.txt",
    "app/api_utils.py",
    "app/chat_interface.py",
    "app/sidebar.py",
    "app/streamlit_app.py"
]

# Loop to create files and folders directly in the current directory
for filepath in list_of_files:
    # Create path directly
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # Create folder if it does not exist
    if filedir != "" and not os.path.exists(filedir):
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    # Create empty file if it does not exist or is empty
    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, 'w') as f:
            pass  # Create empty file
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")