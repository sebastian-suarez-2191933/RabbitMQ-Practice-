# Usa la imagen base oficial de Python
FROM python:3.9-slim

# Copia el script del productor al directorio /app en el contenedor
COPY productor-python.py /app/

# Instala las dependencias necesarias
RUN pip install pika

# Establece el directorio de trabajo en /app
WORKDIR /app

ENV RABBITMQ_USER=scsuarezg
ENV RABBITMQ_PASS=Alaksdjlqnnq

# Ejecuta el script del productor cuando se inicie el contenedor
CMD ["python", "productor-python.py"]
