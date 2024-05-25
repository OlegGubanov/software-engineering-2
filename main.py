from PIL import Image
import streamlit as st
import models


processor, ocr_model = models.load_ocr_models()
tokenizer, spell_check_model = models.load_spell_check_models()

img = st.file_uploader(label="Загрузите изображение")
if img is not None:
    image = Image.open(img)
    pixel_values = processor(images=image, return_tensors="pt").pixel_values
    ids = ocr_model.generate(pixel_values)
    text = processor.batch_decode(ids, skip_special_tokens=True)[0]
    st.text(text)

    inputs = tokenizer(
        text,
        max_length=None,
        padding="longest",
        truncation=False,
        return_tensors="pt",
    )

    outputs = spell_check_model.generate(
        **inputs.to(spell_check_model.device),
        max_length=inputs["input_ids"].size(1) * 1.5
    )

    result = tokenizer.batch_decode(outputs, skip_special_tokens=True)
    st.text(result)
