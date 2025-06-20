# TP_Final_Intro
# Ludoteca
### Flask and Furious

Este es el repositorio para almacenar el trabajo práctico de Introducción al Desarrollo de Software de la Cátedra Lanzillotta, del grupo nro. 17.

## Instalación

El archivo `init.sh` es un script el cual instala todas las dependencias necesarias para el proyecto.

Para levantar la base de datos, se recomienda utilizar Docker o contar con un entorno de MySQL configurado. Luego, se debe ejecutar el script `init_db` para crear las tablas y cargar los datos iniciales.

### Base de Datos con Docker

Si se quiere levantar la base de datos con docker se puede hacer con los siguientes comandos
```
  cd app-backend
  docker-compose up
```
Con esto se va a generar el contenedor de docker con MySQL y a la vez ejecutara el script de creacion de la Base con sus tablas y datos

### Archivo .env
Para la secret_key de la app de Flask usamos la bibloteca dotenv de python para ello se debe agregar un archivo .env en la carpeta de app-frontend/src
Datos: 

SECRET_KEY=_5#y2L"F4Q8z\n\xec]

API_BASE="http://localhost:5000"

_Comandos:_
```
  cd app-frontend/src
  touch .env
  echo SECRET_KEY=_5#y2L"F4Q8z\n\xec] >> .env
  echo API_BASE="http://localhost:5000" >> .env
```
