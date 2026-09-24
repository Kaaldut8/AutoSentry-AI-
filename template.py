from pathlib import Path
import os
import logging


logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

list_of_files = [
    f"src/ingestion/__init__.py",
    f"src/processing/__init__.py",
    f"src/config/__init__.py",
]

list_of_directories = [
    "notebooks",
    "data/raw/",
    "data/processed/",
    "tests",
]

for directory in list_of_directories:
    path = Path(directory)
    path.mkdir(parents=True, exist_ok=True)
    logging.info(f"Directory ready: {path}")

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filename)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filename}")

    else:
        logging.info(f"{filename} is already exists")