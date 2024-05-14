from transformers import TrOCRProcessor, VisionEncoderDecoderModel, AutoTokenizer, AutoModelForSeq2SeqLM
from PIL import Image
import streamlit as st

processor = TrOCRProcessor.from_pretrained('raxtemur/trocr-base-ru', from_pt=True)
text_recognition_model = VisionEncoderDecoderModel.from_pretrained('raxtemur/trocr-base-ru')

tokenizer = AutoTokenizer.from_pretrained("ai-forever/sage-fredt5-distilled-95m")
typos_model = AutoModelForSeq2SeqLM.from_pretrained("ai-forever/sage-fredt5-distilled-95m")

img = st.file_uploader(label='Загрузите изображение')
if img is not None:
    image = Image.open(img)
    pixel_values = processor(images=image, return_tensors="pt").pixel_values
    generated_ids = text_recognition_model.generate(pixel_values)
    generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
    st.text(generated_text)

    inputs = tokenizer(generated_text, max_length=None, padding="longest", truncation=False, return_tensors="pt")
    outputs = typos_model.generate(**inputs.to(typos_model.device), max_length = inputs["input_ids"].size(1) * 1.5)
    result = tokenizer.batch_decode(outputs, skip_special_tokens=True)
    st.text(result)
