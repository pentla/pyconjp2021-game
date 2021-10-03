from api.conf import get_texts, get_questions

texts = get_texts()
questions = get_questions()

def test_text():
    for _, val in texts.items():
        assert val['text'] is not None
        assert val['question'] is not None


def test_question():
    for _, val in questions.items():
        assert val['text'] is not None
        assert val['answer'] is not None
        assert val['nextText'] is not None
