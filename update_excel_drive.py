# Upload Excels to Google Drive using API
# Author: César Rodríguez
# Date: 06/10/2023
# Version: 1.0.0

import os
from Google import Create_Service
from googleapiclient.http import MediaFileUpload

API_NAME = "drive"
API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/drive"]
CLIENT_SECRETS = "insert the path to your JSON credentials here"

service = Create_Service(CLIENT_SECRETS, API_NAME, API_VERSION, SCOPES)

# ID of the folder where you want to upload the files (or leave carpeta_destino as None to upload to the root)
destination_folder_id = None  # Insert the ID of the destination folder in Google Drive or leave as None to upload to the root.

# Local folder you want to upload
local_folder = "insert the path to your local folder here"

# Iterate through all files and folders in the local folder
for root, _, files in os.walk(local_folder):
    for name in files:
        local_file = os.path.join(root, name)
        media = MediaFileUpload(local_file, resumable=True)
        
        file_metadata = {
            "name": name,
            "parents": [destination_folder_id] if destination_folder_id else []  # Destination folder or root
        }

        service.files().create(
            body=file_metadata,
            media_body=media
        ).execute()
