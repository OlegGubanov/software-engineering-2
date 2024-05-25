from load_models import load_ocr_models, load_spell_check_models


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
