# Usar una imagen base que contenga Java
FROM adoptopenjdk:11-jre-hotspot

# Copiar el jar de la aplicación al contenedor
COPY target/consumidor.jar /app/consumidor.jar

# Definir el directorio de trabajo dentro del contenedor
WORKDIR /app

# Exponer el puerto si es necesario
# EXPOSE 8080

ENV RABBITMQ_USER=scsuarezg
ENV RABBITMQ_PASS=Alaksdjlqnnq

# Comando para ejecutar la aplicación cuando se inicie el contenedor
CMD ["java", "-jar", "consumidor.jar"]