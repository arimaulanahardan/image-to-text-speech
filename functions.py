from PIL import Image
import pytesseract
from gtts import gTTS
import os

# Fungsi untuk ekstraksi teks dari gambar menggunakan Tesseract
def extract_text_from_image(image):
    try:
        text = pytesseract.image_to_string(image)
        return text if text else "No text detected."
    except Exception as e:
        return str(e)

# Fungsi untuk mengubah teks menjadi suara dengan gTTS
def convert_text_to_speech(text, output_file="output.mp3"):
    try:
        tts = gTTS(text)
        tts.save(output_file)
        return output_file
    except Exception as e:
        return str(e)

# Fungsi untuk membersihkan file suara setelah diputar
def clean_up_audio(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
