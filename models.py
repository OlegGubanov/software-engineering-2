import config
import streamlit as st
from transformers import (
    TrOCRProcessor,
    VisionEncoderDecoderModel,
    AutoTokenizer,
    AutoModelForSeq2SeqLM,
)


@st.cache_resource
def load_ocr_models():
    model_id = config.OCR_MODEL_ID
    processor = TrOCRProcessor.from_pretrained(model_id, from_pt=True)
    ocr_model = VisionEncoderDecoderModel.from_pretrained(model_id)
    return processor, ocr_model


@st.cache_resource
def load_spell_check_models():
    model_id = config.SPELL_CHECK_MODEL_ID
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    spell_check_model = AutoModelForSeq2SeqLM.from_pretrained(model_id)
    return tokenizer, spell_check_model


def process_image(image):
    recognized_text = recognize_text_from_image(image)
    correct_text = check_spelling_in_text(recognized_text)
    return recognized_text, correct_text


def recognize_text_from_image(image):
    processor, ocr_model = load_ocr_models()
    pixel_values = processor(images=image, return_tensors="pt").pixel_values
    ids = ocr_model.generate(pixel_values)
    text = processor.batch_decode(ids, skip_special_tokens=True)[0]
    return text


def check_spelling_in_text(text):
    tokenizer, spell_check_model = load_spell_check_models()

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

    correct_text = tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]
    return correct_text
