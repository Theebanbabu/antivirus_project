import os
from antivirus.utils.hash_utils import calculate_file_hash
from antivirus.quarantine import quarantine_file
from antivirus.utils.logger import log

def scan_file(file_path, signatures):
    """Scan a file for malware."""
    if not os.path.exists(file_path):
        log(f"File not found: {file_path}", level="error")
        return False

    file_hash = calculate_file_hash(file_path)
    if file_hash in signatures:
        log(f"Malware detected: {file_path} (Hash: {file_hash})", level="warning")
        quarantine_file(file_path)
        return True
    else:
        log(f"File is clean: {file_path}", level="info")
        return False
