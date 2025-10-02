import streamlit as st
from api_utils import upload_document, list_documents, delete_document

def display_sidebar():
    # Sidebar: Model Selection
    model_options = ["gpt-4o", "gpt-4o-mini"]
    st.sidebar.selectbox("Select Model", options=model_options, key="model")

    # Sidebar: Upload Document
    st.sidebar.header("Upload Document")
    uploaded_file = st.sidebar.file_uploader("Choose a file", type=["pdf", "docx", "html"])
    if uploaded_file is not None:
        if st.sidebar.button("Upload"):
            with st.spinner("Uploading and Indexing..."):
                upload_response = upload_document(uploaded_file)
                if upload_response:
                    st.sidebar.success(f"File '{uploaded_file.name}' uploaded successfully with ID {upload_response['file_id']}.")
                    st.session_state.documents = list_documents()

    # Sidebar: List Documents
    st.sidebar.header("Uploaded Documents")
    if st.sidebar.button("Refresh Document List"):
        with st.spinner("Refreshing..."):
            st.session_state.documents = list_documents()

    if "documents" not in st.session_state:
        st.session_state.documents = list_documents()

    documents = st.session_state.documents
    if documents:
        # Create a dictionary for easy lookup of filename by id
        doc_map = {doc['id']: doc['filename'] for doc in documents}

        for doc_id, doc_filename in doc_map.items():
            st.sidebar.text(f"{doc_filename} (ID: {doc_id})")
        
        # Delete Document
        selected_file_id = st.sidebar.selectbox(
            "Select a document to delete", 
            options=list(doc_map.keys()), 
            format_func=lambda x: doc_map[x]
        )
        if st.sidebar.button("Delete Selected Document"):
            with st.spinner("Deleting..."):
                delete_response = delete_document(selected_file_id)
                if delete_response and 'error' not in delete_response:
                    st.sidebar.success(f"Document with ID {selected_file_id} deleted successfully.")
                    st.session_state.documents = list_documents()
                else:
                    error_msg = delete_response.get('error', 'Unknown error.') if delete_response else 'Unknown error.'
                    st.sidebar.error(f"Failed to delete: {error_msg}")