CREATE DATABASE IF NOT EXISTS ludoteca;
USE ludoteca;

CREATE TABLE juegos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    genero VARCHAR(50) NOT NULL,
    precio DOUBLE NOT NULL,
    precio_en_oferta DOUBLE,
    en_oferta BOOLEAN DEFAULT FALSE,
    direccion_imagen VARCHAR(255)
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
    tipo_envio VARCHAR,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE,
    FOREIGN KEY (juego_id) REFERENCES juegos(id) ON DELETE CASCADE
);

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

INSERT INTO items_carrito (estado, usuario_id, juego_id, precio, tipo_envio) VALUES
('en carrito', 2, 1, 29.99, 'virtual'),
('comprado', 2, 5, 19.99, 'virtual'),
('desechado', 3, 2, 69.99, 'domicilio'),
('en carrito', 4, 3, 64.99, 'virtual'),
('en carrito', 4, 6, 14.99, 'domicilio');