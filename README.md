Claro, aqui está um exemplo de README.md para o seu projeto FastAPI com Docker:

```markdown
# FastAPI Project

Este é um projeto básico de uma aplicação FastAPI com autenticação usando JWT, configurada para ser executada em um contêiner Docker.

## Estrutura do Projeto

```
fastapi_project
├── app
│   ├── __init__.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── auth.py
│   └── main.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Configuração e Execução

### Pré-requisitos

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Passos para executar o projeto

1. **Clone o repositório:**

   ```sh
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. **Construir a imagem Docker:**

   ```sh
   docker-compose build
   ```

3. **Iniciar o contêiner Docker:**

   ```sh
   docker-compose up
   ```

4. **A aplicação estará disponível em:**

   ```
   http://127.0.0.1:8000
   ```

## Uso da API

### Criação de um novo usuário

- **Endpoint:** `POST /users/`
- **Corpo da requisição:**

  ```json
  {
    "username": "seu-username",
    "email": "seu-email@example.com",
    "password": "sua-senha"
  }
  ```

- **Exemplo de comando curl:**

  ```sh
  curl -X POST "http://127.0.0.1:8000/users/" -H "Content-Type: application/json" -d '{
    "username": "seu-username",
    "email": "seu-email@example.com",
    "password": "sua-senha"
  }'
  ```

### Autenticação e obtenção do token JWT

- **Endpoint:** `POST /token`
- **Corpo da requisição (form-data):**

  ```json
  {
    "username": "seu-username",
    "password": "sua-senha"
  }
  ```

## Dependências

As dependências do projeto estão listadas no arquivo `requirements.txt`:

### Instruções de Uso do README.md

1. **Clone o repositório**: Baixe o projeto do repositório GitHub.
2. **Construa a imagem Docker**: Use `docker-compose build` para construir a imagem Docker.
3. **Inicie o contêiner Docker**: Use `docker-compose up` para iniciar o contêiner.
4. **Acesse a aplicação**: A aplicação estará disponível em `http://127.0.0.1:8000`.

