import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def validate_txt(file_path, message):
    print(f"Checking TXT file: {file_path}")
    print(f"Expected message: {message}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python validate.py <file> <message>")
        sys.exit(1)

    file_path = sys.argv[1]
    message = sys.argv[2]
    validate_txt(file_path, message)
if __name__ == "__main__":
    main()