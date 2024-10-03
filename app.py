import streamlit as st
from PIL import Image
import os
from functions import extract_text_from_image, convert_text_to_speech, clean_up_audio

st.title("Aplikasi SISANGAR")
st.write("Upload Gambar dan kami akan Mengubahnya menjadi Text dan membacanya dengan SANGAR!")

# Unggah gambar
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Tampilkan gambar yang diunggah
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    # Ekstraksi teks dari gambar
    st.write("Extracting text...")
    text = extract_text_from_image(image)
    
    # Tampilkan teks yang diekstraksi
    st.write("Detected text:")
    st.text(text)
    
    # Jika teks terdeteksi, tampilkan tombol untuk memutar suara
    if text and st.button('Play Text as Speech'):
        output_file = convert_text_to_speech(text)
        
        if os.path.exists(output_file):
            # Putar suara
            audio_file = open(output_file, "rb")
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mp3")
            
            # Hapus file suara setelah diputar
            clean_up_audio(output_file)
        else:
            st.write("Error generating audio.")
