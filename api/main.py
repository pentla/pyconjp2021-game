import os
from typing import Optional
from fastapi import FastAPI, HTTPException
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel
from api.conf import get_texts

ENDPOINT = os.getenv('ENDPOINT', '')
PORT = os.getenv('PORT', 8001)

app = FastAPI(port=PORT)
texts = get_texts()


@app.get('/', response_class=PlainTextResponse)
def root():
    return  f"""
PyconJP 2021 JX通信社の脱出ゲームへようこそ！このゲームはHTTP Requestを用いて問題の出題・回答をします。
ゲームを始める: /question?key=startに対してGETリクエストをする
"""


@app.get('/question', response_class=PlainTextResponse)
def text_root(key: str = ''):
    if key and texts.get(key):
        text = texts[key]['text']
        return text
    return 'keyが設定されていません。keyはテキストのどこかに入っています。'


class QuestionAnswer(BaseModel):
    key: Optional[str]
    answer: str


@app.post('/question')
def question_root(answer: QuestionAnswer):
    if answer.key is None:
        raise HTTPException(status_code=400, detail='keyが入っていません。keyは問題文と同じです')

    if answer.answer is None:
        raise HTTPException(status_code=400, detail='answerが入っていません。answerに対して回答を設定してリクエストしてください。')

    if answer.key and texts.get(answer.key):
        # strで比較する
        if str(answer.answer) == str(texts[answer.key]['answer']):
            return {'text': texts[answer.key]['nextText']}
        raise HTTPException(status_code=400, detail='正解ではありません。')
    raise {'message': 'keyが正しくありません'}
