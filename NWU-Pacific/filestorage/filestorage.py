# -*- coding: utf-8 -*-
"""
Spyder Editor

Documentation for Azure Storage SDK: https://azure-storage.readthedocs.io/
https://docs.microsoft.com/en-us/azure/storage/files/storage-python-how-to-use-file-storage#upload-a-file

"""
import os
from azure.storage.file import FileService
from azure.storage.file import ContentSettings

#need to write a function to get the current file path and upload a file, for now we'll use the current working directory

storageacctname = "complaintsml"
key1 = "5fhQW/+/cG09VyOoinKy80YeV5nPGj1GRDrTo0ucZSS0/rX3SICBf9lV0xyMYQ1HMauKLsPF3wM7gYZQEN7NVw=="
fileshare = "complaintsml-fileshare"

file_service = FileService(account_name=storageacctname, account_key=key1)

def UploadFile(target_directory,file_name,source_path,content_type_str='application/json'):
    #Default file type is json.  for Pickle files, use application/octet-stream
    _content_settings = ContentSettings(content_type=content_type_str)
    
    file_service.create_file_from_path(
            fileshare,
            target_directory,
            file_name,
            source_path,
            content_settings = _content_settings
            )


def UploadFile(target_directory,target_file_name,source_file,content_type_str='application/json'):
    #Default file type is json.  for Pickle files, use application/octet-stream
    #Could add parameters for types of file or overloaded functions, lets see what we need
    #This will work fine for basic upload/download for now
    #Source file needs to be fully qualified location with file name like C:\\Users\\Jeffj\Myfile.json
    
    _content_settings = ContentSettings(content_type=content_type_str)
    
    file_service.create_file_from_path(
            fileshare,
            target_directory,
            target_file_name,
            source_file,
            content_settings = _content_settings
            )

def DownloadFile(source_directory, source_file_name, target_file):
    file_service.get_file_to_path(
            fileshare,
            source_directory,
            source_file_name,
            target_file)
    



#Testing
"""
#try a local json file
UploadFile(target_directory="test",target_file_name="HotelWordCounts.json",source_path="HotelWordCounts.json")

#file in Azure storage called 'downloadtest.txt'
DownloadFile("test","downloadtest.txt","downloadtest.txt")

"""
