from PIL import Image
import streamlit as st
import models


img = st.file_uploader(label="Загрузите изображение", accept_multiple_files=False)
if img is not None:
    image = Image.open(img)
    st.text("Загруженное изображение:")
    st.image(image)

    recognized_text, correct_text = models.process_image(image)
    st.text("Распознанный текст: " + recognized_text)
    st.text("Правильный текст: " + correct_text)

