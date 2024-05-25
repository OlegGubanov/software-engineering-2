from PIL import Image
import streamlit as st
import models


img = st.file_uploader(label="Загрузите изображение")
if img is not None:
    image = Image.open(img)
    recognized_text, correct_text = models.process_image(image)
    st.text(recognized_text)
    st.text(correct_text)
