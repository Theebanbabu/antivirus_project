import os
import shutil

QUARANTINE_DIR = "quarantine"

def quarantine_file(file_path):
    """Move a file to the quarantine directory."""
    if not os.path.exists(QUARANTINE_DIR):
        os.makedirs(QUARANTINE_DIR)

    file_name = os.path.basename(file_path)
    quarantine_path = os.path.join(QUARANTINE_DIR, file_name)

    shutil.move(file_path, quarantine_path)
    print(f"File quarantined: {file_path} -> {quarantine_path}")
