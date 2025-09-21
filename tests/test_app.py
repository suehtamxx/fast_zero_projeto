from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_read_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # arrange(organizacao)

    response = client.get('/')  # act(acao)

    assert response.status_code == HTTPStatus.OK  # assert
    assert response.json() == {'message': 'Hello World!'}


def test_exercicio_ola_mundo_em_html():
    client = TestClient(app)
    response = client.get('/exercicio_html')

    assert response.status_code == HTTPStatus.OK
    assert '<h1>Ola mundo</h1>' in response.text
