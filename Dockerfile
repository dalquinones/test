# Usar una imagen base de Python
FROM python:3.11-slim

RUN apt-get update && apt-get install -y nano

# Establecer el directorio de trabajo en /app
WORKDIR /app

# Copiar el archivo de Python y el archivo de texto a la imagen
COPY src/ ./src/

VOLUME ./app/src

# Comando que se ejecuta al iniciar el contenedor
CMD ["python", "src/infinite_loop.py"]
