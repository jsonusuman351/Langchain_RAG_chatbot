import requests
import streamlit as st

API_URL = "https://langchain-rag-chatbot-l34n.onrender.com"

def get_api_response(question, session_id, model):
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }
    data = {
        "question": question,
        "model": model,
        "session_id": session_id
    }

    try:
        response = requests.post(f"{API_URL}/chat", headers=headers, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"API request failed: {e}")
        return None

def upload_document(file):
    try:
        files = {"file": (file.name, file, file.type)}
        response = requests.post(f"{API_URL}/upload-doc", files=files)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Failed to upload file: {e}")
        return None

def list_documents():
    try:
        response = requests.get(f"{API_URL}/list-docs")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Failed to fetch document list: {e}")
        return []

def delete_document(file_id):
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }
    data = {"file_id": file_id}
    try:
        response = requests.post(f"{API_URL}/delete-doc", headers=headers, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Failed to delete document: {e}")
        return None
