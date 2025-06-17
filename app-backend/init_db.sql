DROP DATABASE IF EXISTS ludoteca;
CREATE DATABASE ludoteca;
USE ludoteca;

CREATE TABLE generos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_genero VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE juegos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre NVARCHAR(50) NOT NULL,
    descripcion NVARCHAR(500) NOT NULL,
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

ALTER DATABASE ludoteca CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;
ALTER TABLE juegos CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    rol VARCHAR(8) NOT NULL,
    usuario VARCHAR(50) NOT NULL UNIQUE,
    contraseña VARCHAR(20) NOT NULL,
    email VARCHAR(50) NOT NULL UNIQUE,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    pais varchar(50) NOT NULL,
    ciudad varchar(50) NOT NULL,
    calle VARCHAR(50),
    direccion VARCHAR(50),
    codigo_postal VARCHAR(15)
);

CREATE TABLE metodos_pago (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    tipo VARCHAR(25) NOT NULL,
    marca VARCHAR(25) NOT NULL,
    numero_tarjeta INT NOT NULL,
    fecha_vencimiento DATE NOT NULL,
    codigo_cvv INT NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE
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


CREATE TABLE usuario_online (
    id INT PRIMARY KEY CHECK (id = 1), -- esto es para que la tabla solo tenga un registro
    usuario_id INT NOT NULL, 
    rol VARCHAR(8),
    usuario VARCHAR(50),
    email VARCHAR(100),
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE 
    -- DELETE CASCADE es para que se elimine el dato de aca automaticamente cuando el usuario original
    -- en la tabla 'usuarios' es eliminado con DELETE
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

INSERT INTO juegos (nombre, tipo, id_genero, fecha_lanzamiento, precio, porcentaje_oferta, en_oferta, puntuacion, direccion_imagen, descripcion) VALUES
('The Witcher 3', 'BASE', 1, '2015-05-19', 59.99, 50, TRUE, 92, 'images/witcher3_1.jpg', "Geralt de Rivia, el cazador de monstruos, busca a su hija adoptiva Ciri, quien es perseguida por la salvaje Cacería, una raza mística que amenaza con destruir el mundo. La búsqueda de Geralt lo lleva a través de un vasto mundo abierto lleno de decisiones morales complejas, donde debe lidiar con la guerra, la política y los monstruos, todo mientras intenta proteger a Ciri y evitar el fin del mundo. "),
('Hogwarts Legacy', 'BASE', 2, '2023-02-10', 74.99, 13, TRUE, 85, 'images/hogwarts_legacy_1.jpg', "Ambientado un siglo antes de los acontecimientos narrados en las novelas de Harry Potter, el título forma parte del universo del Mundo Mágico y pone al jugador en el papel de un estudiante del Colegio Hogwarts de Magia y Hechicería, quien explora una variedad de habilidades y artefactos mágicos. Con la ayuda de otros estudiantes y profesores, el protagonista emprende una travesía para descubrir un antiguo secreto oculto en el universo de la franquicia."),
('Cyberpunk 2077', 'BASE', 1, '2020-12-10', 49.99, 20, TRUE, 78, 'images/cyberpunk.jpg', "La historia sigue la lucha de V, un mercenario de Night City que lidia con las consecuencias de un atraco que salió mal y que resulta en un biochip experimental cibernético que contiene un engrama de la legendaria estrella de rock y terrorista Johnny Silverhand, que amenaza con sobrescribir lentamente la mente de V. A medida que avanza la historia, V y Silverhand deben trabajar juntos para encontrar una manera de separarse y salvar la vida de V."),
('Monster Hunter: World Iceborne', 'DLC', 1, '2019-09-06', 19.99, NULL, FALSE, 88, 'images/monter_hunter_world_iceborne_1.jpg', "Historia completamente nueva: la comisión de investigación se aventura en el Arroyo de Escarcha, que el cazador protagonista deberá explorar. Esta nueva región es completamente nueva por lo que uno de los objetivos más importantes de la comisión es el descubrimiento de nuevos monstruos y vida endémica. Conforme se avance la historia se desvelará el misterio que rodea al Arroyo y a Velkhana."),
('Resident Evil Village', 'BASE', 5, '2021-05-07', 59.99, 25, TRUE, 84, 'images/revillage.jpg', "Retoma la historia de Ethan Winters, quien ahora vive con su esposa Mia en un nuevo lugar tras los eventos de Resident Evil 7. Sin embargo, su vida tranquila se ve interrumpida cuando su hija es secuestrada y se ve envuelto en una pesadilla en un misterioso pueblo europeo. 
La trama se desarrolla en un entorno gótico y tenebroso, donde Ethan debe enfrentarse a criaturas peligrosas y a una secta liderada por Mother Miranda."),
('Stardew Valley', 'BASE', 6, '2016-02-26', 14.99, NULL, FALSE, 89, 'images/stardew.jpg', "El jugador recibe la granja en ruinas que alguna vez poseyó su abuelo.

El lugar entero se encuentra lleno de maleza y árboles, y la única construcción disponible es la vieja casa del abuelo. La tarea del jugador es limpiar la tierra para poder cultivarla y ganar dinero, éste junto con otros materiales le permitirán construir otros tipos de edificios para criar animales o construir máquinas que transforman la materia prima."),
('Doki Doki Literature Club', 'BASE', 4, '2017-09-22', 0.00, NULL, FALSE, 91, 'images/dokidoki.jpg', "En Doki Doki Literature Club! el protagonista es invitado por Sayori, su amiga de la infancia, a unirse al club de literatura de su escuela secundaria, del cual ella es vicepresidenta. Allí conoce a las demás miembros del club: Natsuki, Yuri, y la presidenta del club, Monika.[6]​ El protagonista comienza a participar en las actividades del club, como escribir y compartir poesía, y puede escoger si pasar más tiempo con Sayori, Natsuki o Yuri"),
('Little Nightmares', 'BASE', 5, '2017-04-28', 24.99, 60, TRUE, 83, 'images/little_nightmares_1.jpg', "Descripcion"),
('Animal Crossing: New Horizons', 'BASE', 6, '2020-03-20', 59.99, 17, TRUE, 90, 'images/animal_crossing_new_horizons_1.jpg', "Descripcion"),
('The Elder Scrolls V: Skyrim', 'BASE', 8, '2011-11-10', 50.00, 40, FALSE, 96, 'images/skyrim_1.jpg', "Descripcion"),
('World of Warcraft', 'BASE', 8, '2004-11-23', 25.00, 20, FALSE, 80, 'images/wow_1.jpg', "Descripcion"),
('Final Fantasy XIV Online: A Realm Reborn', 'BASE', 8, '2013-08-27', 19.99, 15, FALSE, 80, 'images/fin_fantasy_1.jpg', "Descripcion"),
('League of Legends', 'BASE', 9, '2009-10-27', 0.00, 0, FALSE, 76, 'images/lol_1.jpg', "Descripcion"),
('F1 25', 'BASE', 10, '2025-05-30', 59.99, 25, FALSE, 94, 'images/f1_1.jpg', "Descripcion"),
('Need for Speed: Most Wanted', 'BASE', 10, '2005-11-15', 19.99, 15, FALSE, 71, 'images/need_for_speed_1.jpg', "Descripcion"),
('Apex Legends', 'BASE', 7, '2019-02-04', 0.00, 0, FALSE, 65, 'images/apex_1.jpg', "Descripcion"),
('Battlefield 2042', 'BASE', 7, '2021-11-19', 59.99, 30, FALSE, 60, 'images/battlefield_2042_1.jpg', "Descripcion"),
('Battlefield 1: Revolution', 'BASE', 7, '2017-08-21', 39.99, 30, FALSE, 75, 'images/battlefield_1_1.jpg', "Descripcion"),
('Battlefield 4', 'BASE', 7, '2013-10-19', 39.99, 30, FALSE, 70, 'images/battlefield_4_1.jpg', "Descripcion"),
('Borderlands 2', 'BASE', 7, '2012-09-17', 4.99, 15, FALSE, 80, 'images/borderlands_2_1.jpg', "Descripcion"),
('Borderlands 3', 'BASE', 7, '2019-09-13', 2.99, 15, FALSE, 65, 'images/borderlands_3_1.jpg', "Descripcion"),
('Borderlands 4', 'BASE', 7, '2025-09-12', 45.00, 20, FALSE, 80, 'images/borderlands_4_1.jpg', "Descripcion"),
('Brawlhalla', 'BASE', 7, '2017-09-17', 0.00, 0, FALSE, 75, 'images/brawlhalla_1.jpg', "Descripcion"),
('Crysis Remastered', 'BASE', 7, '2020-09-18', 29.99, 20, FALSE, 70, 'images/crysis_1_1.jpg', "Descripcion"),
('Crysis 2 Remastered', 'BASE', 7, '2021-09-15', 29.99, 20, FALSE, 80, 'images/crysis_2_1.jpg', "Descripcion"),
('Crysis 3 Remastered', 'BASE', 7, '2021-09-15', 29.99, 20, FALSE, 65, 'images/crysis_3_1.jpg', "Descripcion"),
('DOOM Eternal', 'BASE', 7, '2020-03-20', 39.99, 40, FALSE, 85, 'images/doom_eternal_1.jpg', "Descripcion"),
('DOOM (1993)', 'BASE', 7, '1993-12-10', 9.99, 35, FALSE, 95, 'images/doom_1993_1.jpg', "Descripcion"),
('DOOM II', 'BASE', 7, '1994-09-30', 9.99, 40, FALSE, 95, 'images/doom_ii_1.jpg', "Descripcion"),
('DOOM 3', 'BASE', 7, '2004-08-03', 9.99, 40, FALSE, 80, 'images/doom_3_1.jpg', "Descripcion"),
('Destiny 2', 'BASE', 7, '2017-10-23', 79.99, 60, FALSE, 75, 'images/destiny_2_1.jpg', "Descripcion"),
('Delta Force', 'BASE', 7, '2024-12-04', 0.00, 0, FALSE, 60, 'images/delta_force_1.jpg', "Descripcion"),
('Dead Island 2', 'BASE', 7, '2023-04-21', 49.99, 15, FALSE, 70, 'images/dead_island_2_1.jpg', "Descripcion"),
('Far Cry', 'BASE', 7, '2004-03-23', 9.99, 20, FALSE, 70, 'images/far_cry_1_1.jpg', "Descripcion"),
('Far Cry 2', 'BASE', 7, '2008-10-22', 9.99, 20, FALSE, 70, 'images/far_cry_2_1.jpg', "Descripcion"),
('Far Cry 3', 'BASE', 7, '2012-12-04', 19.99, 30, FALSE, 80, 'images/far_cry_3_1.jpg', "Descripcion"),
('Far Cry 3: Blood Dragon', 'BASE', 7, '2013-05-01', 14.99, 40, FALSE, 80,'images/far_cry_blood_dragon_1.jpg', "Descripcion"),
('Far Cry 4', 'BASE', 7, '2014-11-17', 29.00, 40, FALSE, 75, 'images/far_cry_4_1.jpg', "Descripcion"),
('Far Cry New Dawn', 'BASE', 7, '2019-02-15', 39.99, 50, FALSE, 65, 'images/far_cry_new_dawn_1.jpg',"Descripcion"),
('Far Cry Primal', 'BASE', 7, '2016-02-29', 29.99, 30, FALSE, 65, 'images/far_cry_primal_1.jpg', "Descripcion"),
('Payday 2', 'BASE', 7, '2013-08-13', 12.99, 25, FALSE, 65, 'images/payday_2_1.jpg', "Descripcion"),
('Fortnite', 'BASE', 7, '2017-07-25', 0.00, 0, FALSE, 65, 'images/fortnite_1.jpg', "Descripcion"),
('LEGO Brawls', 'BASE', 7, '2022-09-02', 9.99, 15, FALSE, 75, 'images/lego_brawls_1.jpg', "Descripcion"),
('LIMBO', 'BASE', 7, '2011-08-02', 9.99, 15, FALSE, 75, 'images/limbo_1.jpg', "Descripcion"),
('Cuphead', 'BASE', 7, '2017-09-29', 19.99, 40, FALSE, 80, 'images/cuphead_1.jpg', "Descripcion"),
('Mortal Kombat 1', 'BASE', 7, '2023-09-19', 49.99, 50, FALSE, 60, 'images/mortal_kombat_1.jpg', "Descripcion"),
('ABZU', 'BASE', 2, '2016-08-02', 19.99, 50, FALSE, 65, 'images/abzu_1.jpg', "Descripcion"),
('EA Sports FC 24', 'BASE', 3, '2023-09-29', 69.99, 70, FALSE, 55, 'images/fc_24_1.jpg', "Descripcion"),
('EA Sports FC 25', 'BASE', 3, '2024-09-27', 69.99, 70, FALSE, 55, 'images/fc_25_1.jpg', "Descripcion"),
('Looney Tunes: Wacky World of Sports', 'BASE', 3, '2024-09-27', 49.99, 50, FALSE, 60, 'images/looney_tunes_1.jpg', "Descripcion"),
('NBA 2K21', 'BASE', 3, '2020-09-03', 50.00, 30, FALSE, 50, 'images/nba_2k21_1.jpg', "Descripcion");

INSERT INTO usuarios (rol, usuario, contraseña, email, nombre, apellido, pais, ciudad, calle, direccion, codigo_postal) VALUES
('admin', 'admin', '1234', 'admin@example.com', 'Admin', 'Root', 'Argentina', 'CABA', 'Avenida Central', '123 Piso 1', '1000'),
('final', 'juancito', '4321', 'juan@gmail.com', 'Juan', 'Pérez', 'Argentina','AVELLANEDA', 'Mitre', '4325 Dto 3', '1407');


INSERT INTO items_carrito (estado, usuario_id, juego_id, precio, tipo_envio) VALUES
('pendiente', 2, 1, 59.99, 'digital'),
('pendiente', 2, 2, 79.99, 'fisico'),
('comprado', 2, 3, 49.99, 'digital');

INSERT INTO metodos_pago (usuario_id, tipo, marca, numero_tarjeta, fecha_vencimiento, codigo_cvv) VALUES
(2, "TARJETA DEBITO", "VISA", "12345687", "2028-12-12", "321");