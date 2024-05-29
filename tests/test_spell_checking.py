import models


def test_empty_text():
    text = ''
    correct_text = models.check_spelling_in_text(text)
    assert correct_text == '...'


def test_correct_text():
    correct_text = 'Привет, мир!'
    model_text = models.check_spelling_in_text(correct_text)
    assert model_text == correct_text


def test_punctuation():
    text = 'Наверное в этом предложении не хватает запятой.'
    correct_text = 'Наверное, в этом предложении не хватает запятой.'
    model_text = models.check_spelling_in_text(text)
    assert model_text == correct_text


def test_typos():
    text = 'В этмо предложеини есьт опечтаки.'
    correct_text = 'В этом предложении есть опечатки.'
    model_text = models.check_spelling_in_text(text)
    assert model_text == correct_text


def test_spelling():
    text = 'В этам предложеннии есть ашибки.'
    correct_text = 'В этом предложении есть ошибки.'
    model_text = models.check_spelling_in_text(text)
    assert model_text == correct_text


def test_everything():
    text = 'В этмо придложении навенрое нету оишбок.'
    correct_text = 'В этом предложении, наверное, нет ошибок.'
    model_text = models.check_spelling_in_text(text)
    assert model_text == correct_text


def test_sentence_with_digits():
    text = 'Сейчас 3 часа ночи.'
    model_text = models.check_spelling_in_text(text)
    assert model_text == text
