# CS VITRINE - Backend


```markdown
# FastAPI Project

## Configuração e Execução

### Pré-requisitos

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
```	
### Passos para executar o projeto

1. **Clone o repositório:**

   ```sh
   git clone https://github.com/WalterSilva5/cfit-backend
   ```

2. **Configure as variáveis de ambiente:**

   ```sh
   cp .env_example .env
   ```
    - Crie um arquivo `.env` e configure as variáveis de ambiente conforme necessário.

3. **Construir a imagem Docker:**

   ```sh
   docker-compose build
   ```

4. **Iniciar o contêiner Docker:**

   ```sh
   docker-compose up
   ```

5. **A aplicação estará disponível em:**

   ```
   http://localhost:8000/docs
   ```

##
- ## Seed
o seed.py é responsável por popular o banco de dados com os dados iniciais.

| User: admin@admin.com | Password: admin | Tipo: Admin |
|-----------------------|------------------| ------------|

##
# Uso da API

## Swagger
 - Para acessar a documentação da API, acesse o link: http://localhost:8000/docs
##

