COMPANY: CODTECH IT SOLUTIONS 

NAME: AKKINEPALLI JAHNAVI

INTERN ID: CT06WK30

DOMAIN: CYBER SECURITY & ETHICAL HACKING

DURATION: 6 WEEEKS 

MENTOR: NEELA SANTOSH 

DESCRIPTION:

This Python script is a File Integrity Checker designed to help users monitor the integrity of files in a specified directory. It serves two primary purposes: generating cryptographic hashes for files and checking those files later to detect any modifications, deletions, or additions. This is useful for cybersecurity, system administration, backup verification, or simply ensuring that important files are not tampered with over time.

Main Functionalities:

1.Hash Generation
The script can scan all files within a specified directory (and its subdirectories) and calculate a cryptographic hash (defaulting to SHA-256) for each file. These hashes act as unique digital fingerprints. After the hashes are calculated, they are stored in a JSON file (by default named hashes.json). This stored data serves as a baseline for future integrity checks.

2.Integrity Checking:
The script can later re-scan the files in the directory and re-calculate their hashes. It then compares the newly calculated hashes against the original hashes saved in the JSON file. Based on this comparison, it reports:

Files that have been modified (hash mismatch),

Files that have been deleted (present in original but missing now),

Files that are new (present now but missing from the original record).

How It Works?
1.Hash Calculation:
The script reads each file in binary mode ("rb") and processes it in chunks (4 KB at a time) to avoid memory issues with large files. It uses Python's hashlib module, which supports various hashing algorithms like SHA-256, MD5, SHA-1, etc. (though the default used here is SHA-256 for its strong security properties).

2.JSON Storage:
The file paths and their corresponding hash values are stored in a simple key-value format inside a JSON file. This approach makes the data easily readable, portable, and simple to update if needed.

3.Directory Traversal:
The script uses os.walk() to recursively navigate through all subdirectories of the specified directory, ensuring that every file gets processed without the need for manual specification.

4.Command-Line Interface (CLI)
The script uses argparse to provide a user-friendly command-line interface. The user must specify the directory to monitor using the --dir argument. Depending on the action they want to perform, they can either:

Use --generate to create and save the hashes,

Use --check to verify the integrity against previously saved hashes.

If neither --generate nor --check is specified, the script prompts the user to specify one, ensuring that the user provides clear intent when running the program.

Optional parameters include --hashfile to specify a custom file to save or load hash data instead of the default hashes.json.

Error Handling:
If a file is missing when calculating a hash, the script returns None, helping the check function recognize and report missing files.

If the specified hash file (hashes.json or custom) does not exist when attempting an integrity check, the script will print an error and abort to prevent false results.

Practical Use Cases:
System Administrators can use this to monitor critical system files and detect unauthorized changes.

Software Developers might use it to verify the integrity of files distributed in a software release.

Researchers handling sensitive datasets can ensure that data remains unaltered.

Home Users could even use it to verify that personal documents or media files haven't been accidentally or maliciously modified.

Strengths and Advantages:
Lightweight: No third-party libraries are required.

Customizable: You can easily change the hashing algorithm if needed.

Cross-platform: As it is built on pure Python, it can run on Linux, Windows, or macOS.

Readable Output: The script clearly marks missing, modified, and newly added files for quick analysis.
