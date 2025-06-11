#!/bin/bash

echo 'Creando carpeta "Proyecto"...'

mkdir -p Proyecto
cd Proyecto
mkdir -p static/images static/js static/css templates

echo Instalando paquetes necesarios...

python -m venv .venv
source .venv/Scripts/activate
pip install flask
pip install flask_mail
touch app.py
code .


CREATE DATABASE IF NOT EXISTS ludoteca;
USE ludoteca;

CREATE TABLE juegos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    id_genero INT NOT NULL,
    precio DOUBLE NOT NULL,
    precio_en_oferta DOUBLE,
    en_oferta BOOLEAN DEFAULT FALSE,
    direccion_imagen VARCHAR(255),
    FOREIGN KEY (id_genero) REFERENCES generos(id);
);

CREATE TABLE generos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    rol VARCHAR(8) NOT NULL,
    usuario VARCHAR(50) NOT NULL UNIQUE,
    contraseña VARCHAR(20) NOT NULL,
    email VARCHAR(50) NOT NULL UNIQUE,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    calle VARCHAR(50),
    direccion VARCHAR(50),
    codigo_postal VARCHAR(15)
);

CREATE TABLE items_carrito (
    id INT AUTO_INCREMENT PRIMARY KEY,
    estado VARCHAR(20) NOT NULL,
    usuario_id INT NOT NULL,
    juego_id INT NOT NULL,
    precio DOUBLE NOT NULL,
    tipo_envio VARCHAR(20),
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE,
    FOREIGN KEY (juego_id) REFERENCES juegos(id) ON DELETE CASCADE
);

INSERT INTO generos (nombre) VALUES 
('rpg'), 
('aventura'), 
('deportes'),
('visual novel'),
('terror'),
('cozy');

INSERT INTO juegos (nombre, tipo, genero, precio, precio_en_oferta, en_oferta, direccion_imagen) VALUES
('The Witcher 3', 'BASE', 'RPG', 59.99, 29.99, TRUE, 'images/witcher3.jpg'),
('Hogwarts Legacy', 'BASE', 'Aventura', 74.99, 64.99, TRUE, 'images/hogwarts.jpg'),
('Cyberpunk 2077', 'BASE', 'RPG', 49.99, 39.99, TRUE, 'images/cyberpunk.jpg'),
('Monster Hunter World: Iceborne', 'DLC', 'RPG', 19.99, NULL, FALSE, 'images/mhiceborn.jpg');

INSERT INTO usuarios (rol, usuario, contraseña, email, nombre, apellido, calle, direccion, codigo_postal) VALUES
('admin', 'adminUser', 'admin123', 'admin@example.com', 'Admin', 'Root', 'Avenida Central', '123 Piso 1', '1000'),
('final', 'juancito', 'clave123', 'juan@gmail.com', 'Juan', 'Pérez', 'Mitre', '4325 Dto 3', '1407'),
('final', 'mariar', 'mypass', 'maria@gmail.com', 'María', 'Rodríguez', 'Sarmiento', '800 PB', '1802'),
('final', 'gamerz', 'pass456', 'gamerz@gmail.com', 'Lucas', 'Martínez', 'Corrientes', '4500 1°A', '1225');

INSERT INTO juegos (nombre, tipo, id_genero, precio, precio_en_oferta, en_oferta, direccion_imagen) VALUES
('The Witcher 3', 'BASE', 1, 59.99, 29.99, TRUE, 'images/witcher3.jpg'),
('Hogwarts Legacy', 'BASE', 2, 74.99, 64.99, TRUE, 'images/hogwarts.jpg'),
('Cyberpunk 2077', 'BASE', 1, 49.99, 39.99, TRUE, 'images/cyberpunk.jpg'),
('Monster Hunter World: Iceborne', 'DLC', 1, 19.99, NULL, FALSE, 'images/mhiceborn.jpg'),
('FIFA 24', 'BASE', 3, 69.99, NULL, FALSE, 'images/fifa24.jpg'),
('Resident Evil Village', 'BASE', 5, 59.99, 44.99, TRUE, 'images/revillage.jpg'),
('Stardew Valley', 'BASE', 6, 14.99, NULL, FALSE, 'images/stardew.jpg'),
('Doki Doki Literature Club', 'BASE', 4, 0.00, NULL, FALSE, 'images/dokidoki.jpg'),
('Little Nightmares', 'BASE', 5, 24.99, 9.99, TRUE, 'images/littlenightmares.jpg'),
('Animal Crossing: New Horizons', 'BASE', 6, 59.99, 49.99, TRUE, 'images/animalcrossing.jpg');