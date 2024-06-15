FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

RUN python -c "from src.models import users_model; users_model.Base.metadata.create_all(bind=users_model.engine)"

RUN alembic upgrade head

RUN python seed.py

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]