import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def validate_txt(file_path):
    print(f"Checking TXT file: {file_path}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python validate.py <file>")
        sys.exit(1)

    file_path = sys.argv[1]
    validate_txt(file_path)

if __name__ == "__main__":
    main()