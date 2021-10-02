import os
from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import yaml

ENDPOINT = os.getenv('ENDPOINT', '')
PORT = os.getenv('PORT', 8001)
# if not ENDPOINT:
#     raise Exception('ENDPOINT environment is not defined')

app = FastAPI(port=PORT)

with open('conf/text.yml') as text_file:
    texts = yaml.safe_load(text_file)

with open('conf/question.yml') as question_file:
    questions = yaml.safe_load(question_file)


@app.get('/')
def root():
    return {
        'message': f"""
PyconJP 2021 JX通信社の脱出ゲームへようこそ！このゲームはHTTP Requestを用いて問題の出題・回答をします。
ルールを表示する場合: /ruleに対してGETリクエストをする
ゲームを始める場合: {ENDPOINT}/startに対してGETリクエストをする
"""
    }

@app.get('/rule')
def rule_root():
    return {
        'message': f"""
ここではルールの説明をします。このゲームはHTTP Requestを用いて問題の出題・回答をします。
テキストのエンドポイント '{ENDPOINT}/text?key=start'を入れると最初の文章が出ます。その際のレスポンスには問題文と、回答先のエンドポイントに使うkeyも表示されます。
問題文のエンドポイントは '{ENDPOINT}/question?key='です。keyに入れる内容は文章の'endpoint_key'にあるキーを利用してください。
問題文はテキストのエンドポイントに記載されています。
このエンドポイントに対してGETリクエストすることで問題文の表示ができ、POSTリクエストで回答ができます。POSTリクエストの際はRequest Bodyに'key' と、'answer'を入れてください。
正解の場合はstatusCode: 200(OK)、間違っている場合はstatusCode: 400(Bad Request)が返ります。
"""
    }

@app.get('/text')
def text_root(key: str = ''):
    if key and texts.get(key):
        # textはmust、questionはないときもある
        text = texts[key]['text']
        question = texts[key].get('question', '')
        return {'text': text, 'question': question, 'endpoint_key': question}
    return {'message': 'keyが設定されていません。keyはテキストのどこかに入っています。'}


@app.get('/question')
def question_get(key: str = ''):
    if key and questions.get(key):
        text = questions[key]['text']
        return {'text': text}
    return {'message': 'keyが設定されていません。keyはテキストのどこかに入っています。'}


class QuestionAnswer(BaseModel):
    key: Optional[str]
    answer: str


@app.post('/question')
def question_root(answer: QuestionAnswer):
    if answer.key is None:
        raise HTTPException(status_code=400, detail='keyが入っていません。keyは問題文と同じです')

    if answer.answer is None:
        raise HTTPException(status_code=400, detail='answerが入っていません。answerに対して回答を設定してリクエストしてください。')

    if answer.key and questions.get(answer.key):
        # strで比較する
        if str(answer.answer) == str(questions[answer.key]['answer']):
            return {'text': questions[answer.key]['nextText']}
        raise HTTPException(status_code=400, detail='正解ではありません。')
    return {'message': 'keyが正しくありません'}
