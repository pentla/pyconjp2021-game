from typing import TypedDict, Any
import yaml


class Texts(TypedDict):
    text: str
    question: str


class Question(TypedDict):
    text: str
    answer: Any
    nextText: str


def get_texts() -> Texts:
    with open('conf/text.yml') as text_file:
        return yaml.safe_load(text_file)

def get_questions() -> Question:
    with open('conf/question.yml') as question_file:
        return yaml.safe_load(question_file)