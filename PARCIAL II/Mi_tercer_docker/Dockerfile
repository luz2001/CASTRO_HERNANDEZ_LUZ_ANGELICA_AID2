FROM python:3.8-slim

# Instala las dependencias necesarias
RUN apt-get update && \
    apt-get install -y ansible && \
    rm -rf /var/lib/apt/lists/*

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de requisitos y luego instala las dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de la aplicación al contenedor
COPY . .

# Expone el puerto en el que corre tu aplicación Flask
EXPOSE 5000

# Comando para ejecutar tu aplicación Flask
CMD ["python", "app.py"]

