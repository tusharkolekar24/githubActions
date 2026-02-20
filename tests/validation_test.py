import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.function import extract_metadata, sql_payload, send_data_to_apex, run_shell_script
def validate_txt(file_path, message):
    print(f"Checking TXT file: {file_path}")
    print(f"Expected message: {message}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python validate.py <file> <message>")
        sys.exit(1)

    file_path = sys.argv[1]
    message   = sys.argv[2]
    # validate_txt(file_path, message)
    print("---------------------------------------------------------------")
    print("Selected File: {}".format(file_path))
    status = "Fail to send data to Oracle APEX"
    if "cni" in message.lower():
        metadata = extract_metadata(file_path, message)
        payload  = sql_payload(metadata)
        print("Payload to be sent to Oracle APEX: {}".format(payload))
        status   = send_data_to_apex(payload)

        if file_path.split('.')[-1]=="sh":
            shell_result = run_shell_script(file_path)
            print("Shell Script Output: {}".format(shell_result))

    print("SQL Payload Status:{}".format(status))
    print("---------------------------------------------------------------\n")

if __name__ == "__main__":
    main()