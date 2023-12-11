# Google Drive Excel Uploader

## Purpose

The **Google Drive Excel Uploader** script simplifies the process of uploading Excel files to Google Drive through the Google Drive API. Developed by César Rodríguez, this tool enables efficient management of your files by seamlessly uploading them to a specified folder in your Google Drive.

## How It Works

### Configuration

1. Set up the script by configuring essential parameters, such as the API name, version, scopes, and the path to your JSON credentials.

### Google Drive API Integration

2. Utilizing the Google Drive API, the script establishes a connection to your Google Drive account with the provided credentials.

### File Upload

3. Specify the local folder containing the Excel files you want to upload. The script then iterates through the files and uploads each one to the designated folder in your Google Drive.

## Usage

1. **Setup:**
   - Configure the script with the necessary API parameters and your Google Drive credentials.

2. **Folder Selection:**
   - Define the local folder path containing the Excel files you want to upload.

3. **Execute:**
   - Run the script using a Python interpreter. The script automates the process of uploading Excel files to your Google Drive.

## Example Scenario

Consider a scenario where you regularly need to upload Excel files to a specific folder in your Google Drive. Instead of manually performing this task, the Google Drive Excel Uploader automates the process, saving you time and ensuring your files are consistently organized in your Google Drive.

## Version Information

- **Author:** César Rodríguez
- **Date:** 06/10/2023
- **Version:** 1.0.0

## Notes

- Ensure you have the necessary API credentials (JSON file) and have set up the required Google Drive API access.
- Customize the `destination_folder_id` variable to specify the target folder in Google Drive or leave it as `None` to upload to the root.

Feel free to contribute or provide feedback to enhance the functionality of this script!
