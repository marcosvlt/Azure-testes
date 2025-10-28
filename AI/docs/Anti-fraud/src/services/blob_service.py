import os
import streamlit as st
from src.utilities.Config import Config
from azure.storage.blob import BlobServiceClient

def upload_file_to_blob(file, filename):
    try:
        blob_service_client = BlobServiceClient.from_connection_string(Config.AZURE_STORAGE_CONNECTION_STRING)
        
        blob_client = blob_service_client.get_blob_client(container=Config.CONTAINER_NAME, blob=filename)
        
        blob_client.upload_blob(file, overwrite=True)
        
        return blob_client.url
    except Exception as e:
        st.error(f"Error uploading file to Blob Storage: {e}")
        return None