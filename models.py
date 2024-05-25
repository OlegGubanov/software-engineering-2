import streamlit as st
from transformers import (
    TrOCRProcessor,
    VisionEncoderDecoderModel,
    AutoTokenizer,
    AutoModelForSeq2SeqLM,
)


@st.cache_resource
def load_ocr_models():
    model_id = "raxtemur/trocr-base-ru"
    processor = TrOCRProcessor.from_pretrained(model_id, from_pt=True)
    ocr_model = VisionEncoderDecoderModel.from_pretrained(model_id)
    return processor, ocr_model


@st.cache_resource
def load_spell_check_models():
    model_id = "ai-forever/sage-fredt5-distilled-95m"
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    spell_check_model = AutoModelForSeq2SeqLM.from_pretrained(model_id)
    return tokenizer, spell_check_model
