import hashlib
import os
import json
import argparse

# Function to calculate file hash
def calculate_hash(file_path, algorithm="sha256"):
    hasher = hashlib.new(algorithm)
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(4096):
                hasher.update(chunk)
        return hasher.hexdigest()
    except FileNotFoundError:
        return None

# Function to generate hash values for files
def generate_hashes(directory, hash_file="hashes.json", algorithm="sha256"):
    file_hashes = {}
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hashes[file_path] = calculate_hash(file_path, algorithm)

    with open(hash_file, "w") as f:
        json.dump(file_hashes, f, indent=4)
    print("Hashes saved successfully.")

# Function to check file integrity
def check_integrity(directory, hash_file="hashes.json", algorithm="sha256"):
    if not os.path.exists(hash_file):
        print("Error: No hash record found. Please generate hashes first.")
        return

    with open(hash_file, "r") as f:
        original_hashes = json.load(f)

    current_hashes = {}
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            current_hashes[file_path] = calculate_hash(file_path, algorithm)

    for file_path, original_hash in original_hashes.items():
        current_hash = current_hashes.get(file_path)
        if current_hash is None:
            print(f"[MISSING] {file_path} has been deleted!")
        elif current_hash != original_hash:
            print(f"[MODIFIED] {file_path} has changed!")

    for file_path in current_hashes.keys():
        if file_path not in original_hashes:
            print(f"[NEW] {file_path} was added!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="File Integrity Checker")
    parser.add_argument("--generate", help="Generate hash values for a directory", action="store_true")
    parser.add_argument("--check", help="Check file integrity", action="store_true")
    parser.add_argument("--dir", help="Directory to monitor", required=True)
    parser.add_argument("--hashfile", help="File to store hashes", default="hashes.json")
    args = parser.parse_args()

    if args.generate:
        generate_hashes(args.dir, args.hashfile)
    elif args.check:
        check_integrity(args.dir, args.hashfile)
    else:
        print("Please specify --generate or --check.")
