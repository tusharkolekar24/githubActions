import requests
import json

def send_data_to_apex(payload):
    url = "https://oracleapex.com/ords/wksp_myapi/filedetail/insertdata"

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json"
    }
    
    status_messages = "Fail to send data to Oracle APEX"
    try:
        # 🔹 Send POST request
        response = requests.post(
            url,
            headers=headers,
            data=json.dumps(payload)
        )

        # 🔹 Print results
        # print("Status Code:", response.status_code)
        # print("Response Text:", response.text)
        status_messages = "Successfully sent data to Oracle APEX"
    except Exception as e:
        print("An error occurred:", str(e))

    return status_messages

def sql_payload(metadata):
    payload ={
    "files":[
            {
                "cni": metadata['cni'],
                "file_name": metadata['file_name'],
                "file_subfolder": metadata['file_subfolder'],
                "file_extension": metadata['file_extension'],
                "message":metadata['message'],
            }
        ]
    }
    return payload

def extract_metadata(file_path,messages):
    
    cni = int(messages.split(" ")[0].lower().replace("cni",""))
    file_subfolder = file_path.split("/")[0]
    file_extension = '.'+file_path.split("/")[-1].split(".")[-1]
    filename       = file_path.split("/")[-1]

    # 🔹 Create metadata dictionary
    metadata = {
        "cni": cni,
        "file_name": filename,
        "file_subfolder": file_subfolder,
        "file_extension": file_extension,
        "message":messages
         
    }
    
    return metadata