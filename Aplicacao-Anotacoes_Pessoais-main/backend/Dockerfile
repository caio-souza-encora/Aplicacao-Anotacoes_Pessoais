# Use uma imagem base com Python
FROM python:3.9-slim

# Defina o diretório de trabalho
WORKDIR /app

# Copie o arquivo de requisitos
COPY requirements.txt /app/requirements.txt


# Instale as dependências
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copie o restante do código da aplicação
COPY ./app /app/app/

# Exponha a porta 8000
EXPOSE 8080

# Comando para iniciar a aplicação
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
