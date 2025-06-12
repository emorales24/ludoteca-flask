CREATE DATABASE IF NOT EXISTS ludoteca;
USE ludoteca;


CREATE TABLE generos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_genero VARCHAR(50) NOT NULL UNIQUE
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

INSERT INTO generos (nombre_genero) VALUES 
('rpg'), 
('aventura'), 
('deportes'),
('visual novel'),
('terror'),
('cozy'),
('accion'),
('role-play'),
('strategy'),
('racing');

INSERT INTO juegos (nombre, tipo, id_genero, fecha_lanzamiento, precio, porcentaje_oferta, en_oferta, puntuacion, direccion_imagen) VALUES
('The Witcher 3', 'BASE', 1, '2015-05-19', 59.99, 50, TRUE, 92, 'images/witcher3_1.jpg'),
('Hogwarts Legacy', 'BASE', 2, '2023-02-10', 74.99, 13, TRUE, 85, 'images/hogwarts_legacy_1.jpg'),
('Cyberpunk 2077', 'BASE', 1, '2020-12-10', 49.99, 20, TRUE, 78, 'images/cyberpunk.jpg'),
('Monster Hunter: World Iceborne', 'DLC', 1, '2019-09-06', 19.99, NULL, FALSE, 88, 'images/monter_hunter_world_iceborne_1.jpg'),
('Resident Evil Village', 'BASE', 5, '2021-05-07', 59.99, 25, TRUE, 84, 'images/revillage.jpg'),
('Stardew Valley', 'BASE', 6, '2016-02-26', 14.99, NULL, FALSE, 89, 'images/stardew.jpg'),
('Doki Doki Literature Club', 'BASE', 4, '2017-09-22', 0.00, NULL, FALSE, 91, 'images/dokidoki.jpg'),
('Little Nightmares', 'BASE', 5, '2017-04-28', 24.99, 60, TRUE, 83, 'images/little_nightmares_1.jpg'),
('Animal Crossing: New Horizons', 'BASE', 6, '2020-03-20', 59.99, 17, TRUE, 90, 'images/animal_crossing_new_horizons_1.jpg'),
('The Elder Scrolls V: Skyrim', 'BASE', 8, '2011-11-10', 50.00, 40, FALSE, 96, 'images/skyrim_1.jpg'),
('World of Warcraft', 'BASE', 8, '2004-11-23', 25.00, 20, FALSE, 80, 'images/wow_1.jpg'),
('Final Fantasy XIV Online: A Realm Reborn', 'BASE', 8, '2013-08-27', 19.99, 15, FALSE, 80, 'images/fin_fantasy_1.jpg'),
('League of Legends', 'BASE', 9, '2009-10-27', 0.00, 0, FALSE, 76, 'images/lol_1.jpg'),
('F1 25', 'BASE', 10, '2025-05-30', 59.99, 25, FALSE, 94, 'images/f1_1.jpg'),
('Need for Speed: Most Wanted', 'BASE', 10, '2005-11-15', 19.99, 15, FALSE, 71, 'images/need_for_speed_1.jpg'),
('Apex Legends', 'BASE', 7, '2019-02-04', 0.00, 0, FALSE, 65, 'images/apex_1.jpg'),
('Battlefield 2042', 'BASE', 7, '2021-11-19', 59.99, 30, FALSE, 60, 'images/battlefield_2042_1.jpg'),
('Battlefield 1: Revolution', 'BASE', 7, '2017-08-21', 39.99, 30, FALSE, 75, 'images/battlefield_1_1.jpg'),
('Battlefield 4', 'BASE', 7, '2013-10-19', 39.99, 30, FALSE, 70, 'images/battlefield_4_1.jpg'),
('Borderlands 2', 'BASE', 7, '2012-09-17', 4.99, 15, FALSE, 80, 'images/borderlands_2_1.jpg'),
('Borderlands 3', 'BASE', 7, '2019-09-13', 2.99, 15, FALSE, 65, 'images/borderlands_3_1.jpg'),
('Borderlands 4', 'BASE', 7, '2025-09-12', 45.00, 20, FALSE, 80, 'images/borderlands_4_1.jpg'),
('Brawlhalla', 'BASE', 7, '2017-09-17', 0.00, 0, FALSE, 75, 'images/brawlhalla_1.jpg'),
('Crysis Remastered', 'BASE', 7, '2020-09-18', 29.99, 20, FALSE, 70, 'images/crysis_1_1.jpg'),
('Crysis 2 Remastered', 'BASE', 7, '2021-09-15', 29.99, 20, FALSE, 80, 'images/crysis_2_1.jpg'),
('Crysis 3 Remastered', 'BASE', 7, '2021-09-15', 29.99, 20, FALSE, 65, 'images/crysis_3_1.jpg'),
('DOOM Eternal', 'BASE', 7, '2020-03-20', 39.99, 40, FALSE, 85, 'images/doom_eternal_1.jpg'),
('DOOM (1993)', 'BASE', 7, '1993-12-10', 9.99, 35, FALSE, 95, 'images/doom_1993_1.jpg'),
('DOOM II', 'BASE', 7, '1994-09-30', 9.99, 40, FALSE, 95, 'images/doom_ii_1.jpg'),
('DOOM 3', 'BASE', 7, '2004-08-03', 9.99, 40, FALSE, 80, 'images/doom_3_1.jpg'),
('Destiny 2', 'BASE', 7, '2017-10-23', 79.99, 60, FALSE, 75, 'images/destiny_2_1.jpg'),
('Delta Force', 'BASE', 7, '2024-12-04', 0.00, 0, FALSE, 60, 'images/delta_force_1.jpg'),
('Dead Island 2', 'BASE', 7, '2023-04-21', 49.99, 15, FALSE, 70, 'images/dead_island_2_1.jpg'),
('Far Cry', 'BASE', 7, '2004-03-23', 9.99, 20, FALSE, 70, 'images/far_cry_1_1.jpg'),
('Far Cry 2', 'BASE', 7, '2008-10-22', 9.99, 20, FALSE, 70, 'images/far_cry_2_1.jpg'),
('Far Cry 3', 'BASE', 7, '2012-12-04', 19.99, 30, FALSE, 80, 'images/far_cry_3_1.jpg'),
('Far Cry 3: Blood Dragon', 'BASE', 7, '2013-05-01', 14.99, 40, FALSE, 80,'images/far_cry_blood_dragon_1.jpg'),
('Far Cry 4', 'BASE', 7, '2014-11-17', 29.00, 40, FALSE, 75, 'images/far_cry_4_1.jpg'),
('Far Cry New Dawn', 'BASE', 7, '2019-02-15', 39.99, 50, FALSE, 65, 'images/far_cry_new_dawn_1.jpg'),
('Far Cry Primal', 'BASE', 7, '2016-02-29', 29.99, 30, FALSE, 65, 'images/far_cry_primal_1.jpg'),
('Payday 2', 'BASE', 7, '2013-08-13', 12.99, 25, FALSE, 65, 'images/payday_2_1.jpg'),
('Fortnite', 'BASE', 7, '2017-07-25', 0.00, 0, FALSE, 65, 'images/fortnite_1.jpg'),
('LEGO Brawls', 'BASE', 7, '2022-09-02', 9.99, 15, FALSE, 75, 'images/lego_brawls_1.jpg'),
('LIMBO', 'BASE', 7, '2011-08-02', 9.99, 15, FALSE, 75, 'images/limbo_1.jpg'),
('Cuphead', 'BASE', 7, '2017-09-29', 19.99, 40, FALSE, 80, 'images/cuphead_1.jpg'),
('Mortal Kombat 1', 'BASE', 7, '2023-09-19', 49.99, 50, FALSE, 60, 'images/mortal_kombat_1.jpg'),
('ABZU', 'BASE', 2, '2016-08-02', 19.99, 50, FALSE, 65, 'images/abzu_1.jpg'),
('EA Sports FC 24', 'BASE', 3, '2023-09-29', 69.99, 70, FALSE, 55, 'images/fc_24_1.jpg'),
('EA Sports FC 25', 'BASE', 3, '2024-09-27', 69.99, 70, FALSE, 55, 'images/fc_25_1.jpg'),
('Looney Tunes: Wacky World of Sports', 'BASE', 3, '2024-09-27', 49.99, 50, FALSE, 60, 'images/looney_tunes_1.jpg'),
('NBA 2K21', 'BASE', 3, '2020-09-03', 50.00, 30, FALSE, 50, 'images/nba_2k21_1.jpg');


INSERT INTO usuarios (rol, usuario, contraseña, email, nombre, apellido, calle, direccion, codigo_postal) VALUES
('admin', 'admin', '1234', 'admin@example.com', 'Admin', 'Root', 'Avenida Central', '123 Piso 1', '1000'),
('final', 'juancito', '4321', 'juan@gmail.com', 'Juan', 'Pérez', 'Mitre', '4325 Dto 3', '1407'),