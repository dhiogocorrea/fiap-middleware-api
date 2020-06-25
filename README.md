# FIAP-Middleware-Api

## Waton - fiapdiagnosisapi - Wason

Esse projeto tem o intuito de pegar o resultado derivado do Watson e traduzir para os parâmetros necessários para a API [fiapdiagnosisapi](https://fiapdiagnosisapi.azurewebsites.net/Diagnosis) , e também traduzir a resposta da API de volta para o Watson.


### Como executar (sem docker):

Instale as dependências
```
pip install -r requirements.txt
```

Execute:

```
uvicorn main:app --reload
```

O comando acima irá iniciar uma api na porta 8000.

Após iniciado, acesse a documentação Swagger via:

```
localhost:8000/docs
```

### Como executar (com docker):

Na pasta raiz do projeto, construa o docker

```
docker build -t fiap-middleware-api:latest .
```

Rode o docker mapeando a porta desejada

```
docker run -d --name fiap-middleware-api -p 8889:80 fiap-middleware-api
```

