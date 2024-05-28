import models
import streamlit as st

from PIL import Image
from utils import getFormattedDiff


img = st.file_uploader(label="Загрузите изображение")
if img is not None:
    image = Image.open(img).convert("RGB")
    st.text("Загруженное изображение:")
    st.image(image)

    recognized_text, correct_text = models.process_image(image)
    st.html("Распознанный текст: " + recognized_text)

    formatted_text = getFormattedDiff(recognized_text, correct_text)[1]
    st.html("Правильный текст: " + formatted_text)
