import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.function import extract_metadata, sql_payload, send_data_to_apex
def validate_txt(file_path, message):
    print(f"Checking TXT file: {file_path}")
    print(f"Expected message: {message}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python validate.py <file> <message>")
        sys.exit(1)

    file_path = sys.argv[1]
    message   = sys.argv[2]
    validate_txt(file_path, message)
    status = "Fail to send data to Oracle APEX"
    if "cni" in message.lower():
        metadata = extract_metadata(file_path, message)
        payload = sql_payload(metadata)
        status = send_data_to_apex(payload)
        print(status)
    print("SQL Payload Status:{}".format(status))
    
if __name__ == "__main__":
    main()