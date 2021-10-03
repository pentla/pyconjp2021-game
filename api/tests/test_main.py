from api.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_root():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json().get('message') is not None


def test_rule():
    response = client.get('/rule')
    assert response.status_code == 200
    assert response.json().get('message') is not None


def test_text_root():
    response = client.get('/text')
    assert response.status_code == 200
    assert 'keyが設定されていません' in response.json().get('message')

    response = client.get('/text', params={'key': 'a'})
    assert response.status_code == 200
    print(response.json())
    assert 'ここにテキストが入ります。' in response.json().get('text')
    assert response.json().get('endpoint_key') is not None


def test_question():
    response = client.get('/question')
    assert response.status_code == 200
    assert 'keyが設定されていません' in response.json().get('message')

    response = client.get('/question', params={'key': 'question1'})
    assert response.status_code == 200
    assert 'これは問題文です。' in response.json().get('text')


def test_post_question():
    response = client.post('/question')
    print(response.json())
    assert response.status_code == 400
    assert 'keyが入っていません' in response.json().get('detail')
