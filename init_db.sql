CREATE DATABASE IF NOT EXISTS ludoteca;
USE ludoteca;

CREATE TABLE juegos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    tipo_id VARCHAR(50) NOT NULL,
    genero VARCHAR(50) NOT NULL,
    precio DOUBLE NOT NULL,
    precio_en_oferta INT,
    en_oferta BOOLEAN DEFAULT FALSE,
    direccion_imagen VARCHAR(255)
);

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    rol VARCHAR(50) NOT NULL,
    usuario VARCHAR(100) NOT NULL UNIQUE,
    contraseña VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    direccion_id VARCHAR(255),
    codigo_postal VARCHAR(20)
);

CREATE TABLE items_carrito (
    id INT AUTO_INCREMENT PRIMARY KEY,
    estado VARCHAR(50) NOT NULL,
    usuario_id INT NOT NULL,
    juego_id INT NOT NULL,
    precio DOUBLE NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE,
    FOREIGN KEY (juego_id) REFERENCES juegos(id) ON DELETE CASCADE
);