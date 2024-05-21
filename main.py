from transformers import (
    TrOCRProcessor,
    VisionEncoderDecoderModel,
    AutoTokenizer,
    AutoModelForSeq2SeqLM,
)
from PIL import Image
import streamlit as st

ocr_model_id = "raxtemur/trocr-base-ru"
processor = TrOCRProcessor.from_pretrained(ocr_model_id, from_pt=True)
ocr_model = VisionEncoderDecoderModel.from_pretrained(ocr_model_id)

spell_check_model_id = "ai-forever/sage-fredt5-distilled-95m"
tokenizer = AutoTokenizer.from_pretrained(spell_check_model_id)
spell_check_model = AutoModelForSeq2SeqLM.from_pretrained(spell_check_model_id)

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
