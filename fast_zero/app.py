from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

from fast_zero.schemas import Message


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Hello World!'}


@app.get('/exercicio_html', response_class=HTMLResponse)
def exercicio_aula_02():
    return """
			<html>
      	<head>
      		<title>Teste</title>
      	</head>
      	<body>
        	<h1>Ola mundo</h1>
      	</body>
      </html>
		"""
