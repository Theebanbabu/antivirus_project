import os

def load_signatures(signature_file):
    """Load malware signatures from a file."""
    if not os.path.exists(signature_file):
        print(f"Signature file '{signature_file}' not found. Creating an empty one.")
        open(signature_file, 'w').close()
    with open(signature_file, 'r') as f:
        return f.read().splitlines()
