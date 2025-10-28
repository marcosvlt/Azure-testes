import streamlit as st
from src.services.blob_service import upload_file_to_blob
from src.services.credit_card_service import analyze_credit_card

def configure_interface():
    st.title("Document Fraud Detection")
    st.write("Upload your documents to check for potential fraud.")
    uploaded_file = st.file_uploader("Choose a document", type=["pdf", "jpg", "png"])

    if uploaded_file is not None:
        fileName = uploaded_file.name
        st.success("File uploaded successfully!")
        # Sent to azure storage and further processing would go here
        blob_url = upload_file_to_blob(uploaded_file, fileName)
        if blob_url is not None:
            st.write(f"File stored at: {blob_url}")
            credit_card_info = analyze_credit_card(blob_url)
            show_image_and_validation(blob_url, credit_card_info)
        else:
            st.error("Failed to store the file.")
    
def show_image_and_validation(image_url, credit_card_info):
    st.image(image_url, caption="Uploaded Document", use_container_width=True)
    st.write("Credit Card Validation:")
    if credit_card_info and credit_card_info.get("card_name"):
        st.write(f"Card Holder Name: {credit_card_info.get('card_name')}")
        st.write(f"Card Number: {credit_card_info.get('card_number')}")
        st.write(f"Expiry Date: {credit_card_info.get('expiry_date')}")
    else:
        st.error("No valid credit card information found.")



if __name__ == "__main__":
    configure_interface()   