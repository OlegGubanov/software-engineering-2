import models
import pytest
from PIL import Image


@pytest.mark.parametrize(
    "filename, expected",
    [
        ("1.png", "Заявление"),
        ("2.png", "вороненый зрачок"),
        ("3.png", "запад."),
        ("4.png", "Проект по программной инженерии"),
        ("5.png", "думаю тут нету ашибок")
    ]
)
def test_recognition(filename, expected):
    image = Image.open(f"examples/{filename}").convert("RGB")
    text = models.recognize_text_from_image(image)
    assert text == expected
