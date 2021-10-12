from typing import TypedDict, Any
import yaml


class Texts(TypedDict):
    text: str
    question: str
    answer: Any
    nextText: str


def get_texts() -> Texts:
    with open('conf/text.yml') as text_file:
        return yaml.safe_load(text_file)
