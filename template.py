import os
from pathlib import Path
import logging

# Configure logging for the application. This will help track file and directory creation events.
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Define the list of required files and directories for the project structure.
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
    "app/streamlit_app.py",
    "app/requirements.txt",
    "docs/" # Directory for document uploads
]

# Iterate over the list and create missing files and directories as needed.
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # Ensure the directory exists before creating files inside it.
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Directory created: {filedir} for file {filename}")

    # Create an empty file if it does not exist or is currently empty.
    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, 'w') as f:
            pass  # File created as a placeholder for future content
            logging.info(f"Empty file created: {filepath}")
    else:
        logging.info(f"File already exists: {filename}")