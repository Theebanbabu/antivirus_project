from antivirus.core.signatures import load_signatures
from antivirus.core.monitor import monitor_system
from antivirus.utils.logger import setup_logger

def main():
    setup_logger()
    signature_file = "malware_signatures.txt"
    signatures = load_signatures(signature_file)

    if not signatures:
        print("No malware signatures found. Add hashes to 'malware_signatures.txt'.")

    monitor_system(signatures)

if __name__ == "__main__":
    main()
