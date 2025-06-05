CREATE DATABASE IF NOT EXISTS ludoteca;
USE ludoteca;


CREATE TABLE generos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE juegos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    id_genero INT NOT NULL,
    fecha_lanzamiento DATE,
    precio DOUBLE NOT NULL,
    porcentaje_oferta INT,
    en_oferta BOOLEAN DEFAULT FALSE,
    puntuacion INT,
    direccion_imagen VARCHAR(255),
    FOREIGN KEY (id_genero) REFERENCES generos(id)
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

INSERT INTO juegos (nombre, tipo, id_genero, fecha_lanzamiento, precio, porcentaje_oferta, en_oferta, puntuacion, direccion_imagen) VALUES
('The Witcher 3', 'BASE', 1, '2015-05-19', 59.99, 50, TRUE, 92, 'images/witcher3.jpg'),
('Hogwarts Legacy', 'BASE', 2, '2023-02-10', 74.99, 13, TRUE, 85, 'images/hogwarts.jpg'),
('Cyberpunk 2077', 'BASE', 1, '2020-12-10', 49.99, 20, TRUE, 78, 'images/cyberpunk.jpg'),
('Monster Hunter World: Iceborne', 'DLC', 1, '2019-09-06', 19.99, NULL, FALSE, 88, 'images/mhiceborn.jpg'),
('Resident Evil Village', 'BASE', 5, '2021-05-07', 59.99, 25, TRUE, 84, 'images/revillage.jpg'),
('Stardew Valley', 'BASE', 6, '2016-02-26', 14.99, NULL, FALSE, 89, 'images/stardew.jpg'),
('Doki Doki Literature Club', 'BASE', 4, '2017-09-22', 0.00, NULL, FALSE, 91, 'images/dokidoki.jpg'),
('Little Nightmares', 'BASE', 5, '2017-04-28', 24.99, 60, TRUE, 83, 'images/littlenightmares.jpg'),
('Animal Crossing: New Horizons', 'BASE', 6, '2020-03-20', 59.99, 17, TRUE, 90, 'images/animalcrossing.jpg');

INSERT INTO usuarios (rol, usuario, contraseña, email, nombre, apellido, calle, direccion, codigo_postal) VALUES
('admin', 'adminUser', 'admin123', 'admin@example.com', 'Admin', 'Root', 'Avenida Central', '123 Piso 1', '1000'),
('final', 'juancito', 'clave123', 'juan@gmail.com', 'Juan', 'Pérez', 'Mitre', '4325 Dto 3', '1407'),
('final', 'mariar', 'mypass', 'maria@gmail.com', 'María', 'Rodríguez', 'Sarmiento', '800 PB', '1802'),
('final', 'gamerz', 'pass456', 'gamerz@gmail.com', 'Lucas', 'Martínez', 'Corrientes', '4500 1°A', '1225');