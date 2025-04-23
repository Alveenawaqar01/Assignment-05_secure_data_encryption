import streamlit as st
from cryptography.fernet import Fernet

# Title
st.title("🔐 Secure Data Encryption App")

# Generate or use existing key
key_placeholder = st.empty()
if 'key' not in st.session_state:
    st.session_state.key = Fernet.generate_key()

fernet = Fernet(st.session_state.key)

# Show encryption key (optional)
if st.checkbox("Show encryption key"):
    key_placeholder.code(st.session_state.key.decode())

# Select operation
option = st.radio("Select Operation", ["Encrypt", "Decrypt"])

# Input text
user_input = st.text_area("Enter text here:")

# Process button
if st.button("Process"):
    if option == "Encrypt":
        try:
            encrypted = fernet.encrypt(user_input.encode()).decode()
            st.success("🔐 Encrypted Text:")
            st.code(encrypted)
        except Exception as e:
            st.error(f"Encryption failed: {e}")
    elif option == "Decrypt":
        try:
            decrypted = fernet.decrypt(user_input.encode()).decode()
            st.success("🔓 Decrypted Text:")
            st.code(decrypted)
        except Exception as e:
            st.error("Decryption failed. Make sure you provided encrypted text and correct key.")

# Button to regenerate key
if st.button("🔁 Generate New Encryption Key"):
    st.session_state.key = Fernet.generate_key()
    st.success("New key generated!")
