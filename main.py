import streamlit as st
import base64

# Title of the app
st.title("🔐 Simple Encryption & Decryption")

# Encryption function
def encrypt(text):
    # Encoding the text into bytes, then encoding it to base64
    encoded_bytes = base64.b64encode(text.encode('utf-8'))
    encoded_str = encoded_bytes.decode('utf-8')
    return encoded_str

# Decryption function
def decrypt(encoded_text):
    # Decoding the base64 encoded text to its original form
    decoded_bytes = base64.b64decode(encoded_text)
    decoded_str = decoded_bytes.decode('utf-8')
    return decoded_str

# Select operation
operation = st.radio("Choose Operation", ["Encrypt", "Decrypt"])

# Input text
text_input = st.text_area("Enter Text:")

# Process the input based on chosen operation
if st.button("Process"):
    if operation == "Encrypt" and text_input:
        encrypted_text = encrypt(text_input)
        st.success("Encrypted Text:")
        st.code(encrypted_text)
    
    elif operation == "Decrypt" and text_input:
        try:
            decrypted_text = decrypt(text_input)
            st.success("Decrypted Text:")
            st.code(decrypted_text)
        except Exception as e:
            st.error("Error: Unable to decode. Ensure the text is properly encoded.")
    else:
        st.warning("Please enter some text to encrypt or decrypt.")
