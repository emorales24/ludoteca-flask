DROP DATABASE IF EXISTS ludoteca;
CREATE DATABASE ludoteca;
USE ludoteca;

CREATE TABLE generos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_genero VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE juegos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    descripcion VARCHAR(500) NOT NULL,
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
    contra VARCHAR(20) NOT NULL,
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
('Stardew Valley', 'BASE', 6, '2016-02-26', 14.99, NULL, FALSE, 89, 'images/stardew.jpg', "El jugador recibe la granja en ruinas que alguna vez poseyó su abuelo. El lugar entero se encuentra lleno de maleza y árboles, y la única construcción disponible es la vieja casa del abuelo. La tarea del jugador es limpiar la tierra para poder cultivarla y ganar dinero, éste junto con otros materiales le permitirán construir otros tipos de edificios para criar animales o construir máquinas que transforman la materia prima."),
('Doki Doki Literature Club', 'BASE', 4, '2017-09-22', 0.00, NULL, FALSE, 91, 'images/dokidoki.jpg', "En Doki Doki Literature Club! el protagonista es invitado por Sayori, su amiga de la infancia, a unirse al club de literatura de su escuela secundaria, del cual ella es vicepresidenta. Allí conoce a las demás miembros del club: Natsuki, Yuri, y la presidenta del club, Monika.[6]​ El protagonista comienza a participar en las actividades del club, como escribir y compartir poesía, y puede escoger si pasar más tiempo con Sayori, Natsuki o Yuri"),
('Little Nightmares', 'BASE', 5, '2017-04-28', 24.99, 60, TRUE, 83, 'images/little_nightmares_1.jpg', "Embárcate en una oscura y caprichosa aventura donde ayudarás a Six a escapar de Las Fauces, un vasto y misterioso navío habitado por almas corruptas en busca de su próxima comida. Explora un mundo perturbador y enfrenta tus miedos de la infancia en este juego de plataformas y puzles."),
('Animal Crossing: New Horizons', 'BASE', 6, '2020-03-20', 59.99, 17, TRUE, 90, 'images/animal_crossing_new_horizons_1.jpg', "¡Escapa a una isla desierta y crea tu propio paraíso mientras exploras, creas y personalizas en Animal Crossing: New Horizons! Tu nueva vida está llena de posibilidades, desde decorar tu hogar hasta compartir la experiencia con amigos."),
('The Elder Scrolls V: Skyrim', 'BASE', 8, '2011-11-10', 50.00, 40, FALSE, 96, 'images/skyrim_1.jpg', "Gana tu destino como Dovahkiin, el Sangre de Dragón, y salva a Skyrim de la destrucción. Explora un mundo abierto épico, lucha contra dragones y elige tu propio camino en esta aclamada aventura de rol."),
('World of Warcraft', 'BASE', 8, '2004-11-23', 25.00, 20, FALSE, 80, 'images/wow_1.jpg', "Únete a millones de jugadores en un mundo de mitos, magia y aventuras sin fin. Explora Azeroth, enfréntate a poderosos enemigos y forja tu propia leyenda en el MMORPG más popular del mundo."),
('Final Fantasy XIV Online: A Realm Reborn', 'BASE', 8, '2013-08-27', 19.99, 15, FALSE, 80, 'images/fin_fantasy_1.jpg', "Únete a millones de aventureros en Eorzea y vive una historia épica en constante evolución. Personaliza tu personaje, explora un vasto mundo y participa en batallas emocionantes en este MMORPG galardonado."),
('League of Legends', 'BASE', 9, '2009-10-27', 0.00, 0, FALSE, 76, 'images/lol_1.jpg', "League of Legends es un juego de estrategia en equipo donde dos equipos de cinco poderosos campeones se enfrentan para destruir la base del otro. Elige entre más de 140 campeones para realizar jugadas épicas, asegurar asesinatos y derribar torres."),
('F1 25', 'BASE', 10, '2025-05-30', 59.99, 25, FALSE, 94, 'images/f1_1.jpg', "Siente la emoción de la Fórmula 1 en F1 25, con todos los equipos, pilotos y circuitos oficiales del Campeonato Mundial de Fórmula 1 de la FIA 2025. Experimenta la simulación de carreras más realista y desafiante."),
('Need for Speed: Most Wanted', 'BASE', 10, '2005-11-15', 19.99, 15, FALSE, 71, 'images/need_for_speed_1.jpg', "Corre, persigue y escapa de la policía en Need for Speed: Most Wanted. Demuestra tus habilidades al volante, personaliza tus coches y conviértete en el piloto más buscado de la ciudad."),
('Apex Legends', 'BASE', 7, '2019-02-04', 0.00, 0, FALSE, 65, 'images/apex_1.jpg', "Apex Legends es un shooter battle royale gratuito donde personajes legendarios con habilidades poderosas se unen para luchar por la fama y la fortuna en los confines de la Frontera."),
('Battlefield 2042', 'BASE', 7, '2021-11-19', 59.99, 30, FALSE, 60, 'images/battlefield_2042_1.jpg', "Battlefield™ 2042 es un shooter en primera persona que marca el regreso a la emblemática guerra total de la franquicia. Adáptate y supera campos de batalla dinámicos con la ayuda de tu escuadrón y un arsenal de vanguardia."),
('Battlefield 1: Revolution', 'BASE', 7, '2017-08-21', 39.99, 30, FALSE, 75, 'images/battlefield_1_1.jpg', "Vive la guerra total en Battlefield 1 Revolution. Descubre el origen de la guerra moderna en una campaña épica y participa en intensas batallas multijugador ambientadas en la Primera Guerra Mundial."),
('Battlefield 4', 'BASE', 7, '2013-10-19', 39.99, 30, FALSE, 70, 'images/battlefield_4_1.jpg', "Battlefield 4™ es el referente de la acción bélica, con momentos que difuminan la línea entre el juego y la gloria. Con entornos destructibles, vehículos y la intensidad de la guerra total, vive la experiencia definitiva de Battlefield."),
('Borderlands 2', 'BASE', 7, '2012-09-17', 4.99, 15, FALSE, 80, 'images/borderlands_2_1.jpg', "Disfruta de la galardonada combinación de acción y rol en Borderlands 2. Juega solo o en cooperativo, explora Pandora, derrota enemigos y consigue millones de armas en este shooter de locura desenfrenada."),
('Borderlands 3', 'BASE', 7, '2019-09-13', 2.99, 15, FALSE, 65, 'images/borderlands_3_1.jpg', "La locura regresa en Borderlands 3. Juega solo o en cooperativo, enfréntate a enemigos y jefes épicos, consigue toneladas de botín y salva tu hogar de los líderes de culto más despiadados de la galaxia."),
('Borderlands 4', 'BASE', 7, '2025-09-12', 45.00, 20, FALSE, 80, 'images/borderlands_4_1.jpg', "¡La próxima entrega de la saga Borderlands! Prepárate para más caos, armas y aventuras en un nuevo capítulo lleno de acción y humor característico de la franquicia."),
('Brawlhalla', 'BASE', 7, '2017-09-17', 0.00, 0, FALSE, 75, 'images/brawlhalla_1.jpg', "Brawlhalla es un juego de lucha de plataformas gratuito con más de 80 millones de jugadores. Únete a partidas en línea, locales o personalizadas y demuestra tus habilidades en combates épicos."),
('Crysis Remastered', 'BASE', 7, '2020-09-18', 29.99, 20, FALSE, 70, 'images/crysis_1_1.jpg', "El clásico shooter en primera persona regresa con gráficos remasterizados. Enfréntate a soldados enemigos, alienígenas y utiliza tu nanotraje para sobrevivir en una isla hostil."),
('Crysis 2 Remastered', 'BASE', 7, '2021-09-15', 29.99, 20, FALSE, 80, 'images/crysis_2_1.jpg', "La invasión alienígena ha devastado Nueva York. Solo tú tienes la tecnología para sobrevivir. Equípate con el nanotraje y salva a la humanidad en esta versión remasterizada del clásico shooter."),
('Crysis 3 Remastered', 'BASE', 7, '2021-09-15', 29.99, 20, FALSE, 65, 'images/crysis_3_1.jpg', "Enfréntate a la amenaza definitiva en Crysis 3 Remastered. Usa el nanotraje para cazar a tus enemigos en un mundo abierto y devastado, y descubre la verdad detrás de la invasión."),
('DOOM Eternal', 'BASE', 7, '2020-03-20', 39.99, 40, FALSE, 85, 'images/doom_eternal_1.jpg', "¡El infierno ha llegado a la Tierra! Conviértete en el Slayer y derrota a demonios en dimensiones épicas en este shooter frenético y brutal."),
('DOOM (1993)', 'BASE', 7, '1993-12-10', 9.99, 35, FALSE, 95, 'images/doom_1993_1.jpg', "El clásico que lo empezó todo. Enfréntate a hordas de demonios y explora laberintos infernales en este shooter en primera persona que definió un género."),
('DOOM II', 'BASE', 7, '1994-09-30', 9.99, 40, FALSE, 95, 'images/doom_ii_1.jpg', "La secuela del legendario DOOM. Más demonios, más armas y más acción en este clásico de los shooters."),
('DOOM 3', 'BASE', 7, '2004-08-03', 9.99, 40, FALSE, 80, 'images/doom_3_1.jpg', "Una reinvención oscura y aterradora del clásico DOOM. Sobrevive a horrores inimaginables en la base de Marte y enfréntate a tus peores pesadillas."),
('Destiny 2', 'BASE', 7, '2017-10-23', 79.99, 60, FALSE, 75, 'images/destiny_2_1.jpg', "Destiny 2 es un shooter de acción multijugador en línea. Explora los misterios de nuestro sistema solar, personaliza tu Guardián y lucha para recuperar la Luz."),
('Delta Force', 'BASE', 7, '2024-12-04', 0.00, 0, FALSE, 60, 'images/delta_force_1.jpg', "Delta Force regresa con acción táctica moderna. Lidera a tu escuadrón en misiones de alto riesgo y demuestra tu destreza en el campo de batalla."),
('Dead Island 2', 'BASE', 7, '2023-04-21', 49.99, 15, FALSE, 70, 'images/dead_island_2_1.jpg', "Sobrevive a un apocalipsis zombi en Los Ángeles. Personaliza armas, mejora tus habilidades y enfréntate a hordas de muertos vivientes en este sangriento y divertido juego de acción."),
('Far Cry', 'BASE', 7, '2004-03-23', 9.99, 20, FALSE, 70, 'images/far_cry_1_1.jpg', "Enfréntate a mercenarios y criaturas mutantes en una isla tropical. Usa tu ingenio y arsenal para sobrevivir en este shooter en primera persona."),
('Far Cry 2', 'BASE', 7, '2008-10-22', 9.99, 20, FALSE, 70, 'images/far_cry_2_1.jpg', "Viaja a África y sobrevive en un mundo abierto lleno de peligros. Cumple misiones, haz aliados y enfréntate a la malaria en este intenso shooter."),
('Far Cry 3', 'BASE', 7, '2012-12-04', 19.99, 30, FALSE, 80, 'images/far_cry_3_1.jpg', "Despierta en una isla tropical controlada por piratas. Salva a tus amigos, enfréntate a villanos memorables y explora un mundo abierto lleno de peligros."),
('Far Cry 3: Blood Dragon', 'BASE', 7, '2013-05-01', 14.99, 40, FALSE, 80,'images/far_cry_blood_dragon_1.jpg', "Una parodia retro-futurista de los años 80. Juega como el sargento Rex Colt y enfréntate a dragones cibernéticos en una aventura llena de acción y humor."),
('Far Cry 4', 'BASE', 7, '2014-11-17', 29.00, 40, FALSE, 75, 'images/far_cry_4_1.jpg', "Viaja a Kyrat, una región salvaje del Himalaya, y enfréntate a un dictador en este shooter de mundo abierto lleno de acción y sorpresas."),
('Far Cry New Dawn', 'BASE', 7, '2019-02-15', 39.99, 50, FALSE, 65, 'images/far_cry_new_dawn_1.jpg',"Secuela de Far Cry 5. Sobrevive en un mundo postapocalíptico, construye tu base y enfréntate a nuevas amenazas en este colorido shooter."),
('Far Cry Primal', 'BASE', 7, '2016-02-29', 29.99, 30, FALSE, 65, 'images/far_cry_primal_1.jpg', "Viaja a la Edad de Piedra y sobrevive como Takkar, el último cazador de su tribu. Domina bestias, crea armas y conquista la tierra de Oros."),
('Payday 2', 'BASE', 7, '2013-08-13', 12.99, 25, FALSE, 65, 'images/payday_2_1.jpg', "PAYDAY 2 es un shooter cooperativo para cuatro jugadores lleno de acción, donde los jugadores asumen el papel de criminales que realizan atracos y robos en todo Washington D.C."),
('Fortnite', 'BASE', 7, '2017-07-25', 0.00, 0, FALSE, 65, 'images/fortnite_1.jpg', "Fortnite es un juego multijugador gratuito donde puedes construir, luchar y sobrevivir en modos Battle Royale, Creativo y Salvar el Mundo."),
('LEGO Brawls', 'BASE', 7, '2022-09-02', 9.99, 15, FALSE, 75, 'images/lego_brawls_1.jpg', "LEGO® Brawls es un juego de lucha multijugador en el que puedes construir tu propio luchador LEGO y competir en arenas inspiradas en los sets clásicos de LEGO."),
('LIMBO', 'BASE', 7, '2011-08-02', 9.99, 15, FALSE, 75, 'images/limbo_1.jpg', "LIMBO es un galardonado juego de plataformas y puzles, conocido por su atmósfera inquietante y su estilo visual minimalista en blanco y negro."),
('Cuphead', 'BASE', 7, '2017-09-29', 19.99, 40, FALSE, 80, 'images/cuphead_1.jpg', "Cuphead es un juego de acción clásico centrado en batallas contra jefes. Inspirado en los dibujos animados de los años 30, presenta gráficos y audio creados con técnicas de la época."),
('Mortal Kombat 1', 'BASE', 7, '2023-09-19', 49.99, 50, FALSE, 60, 'images/mortal_kombat_1.jpg', "Descubre un renacimiento del universo Mortal Kombat creado por el Dios del Fuego Liu Kang. Lucha con un elenco de personajes legendarios y nuevas mecánicas de combate."),
('ABZU', 'BASE', 2, '2016-08-02', 19.99, 50, FALSE, 65, 'images/abzu_1.jpg', "Sumérgete en un vibrante mundo submarino lleno de misterio y color. Descubre criaturas, explora ruinas y experimenta la belleza del océano en esta aventura relajante."),
('EA Sports FC 24', 'BASE', 3, '2023-09-29', 69.99, 70, FALSE, 55, 'images/fc_24_1.jpg', "EA SPORTS FC™ 24 es la nueva era del fútbol. Disfruta de la experiencia más auténtica con más de 19,000 jugadores, 700 equipos y 30 ligas en el juego."),
('EA Sports FC 25', 'BASE', 3, '2024-09-27', 69.99, 70, FALSE, 55, 'images/fc_25_1.jpg', "La próxima entrega de la saga EA SPORTS FC™, con mejoras en jugabilidad, gráficos y modos de juego para los fanáticos del fútbol."),
('Looney Tunes: Wacky World of Sports', 'BASE', 3, '2024-09-27', 49.99, 50, FALSE, 60, 'images/looney_tunes_1.jpg', "¡Juega con tus personajes favoritos de Looney Tunes en una variedad de deportes y desafíos llenos de diversión y locura!"),
('NBA 2K21', 'BASE', 3, '2020-09-03', 50.00, 30, FALSE, 50, 'images/nba_2k21_1.jpg', "NBA 2K21 ofrece una experiencia de baloncesto única con gráficos mejorados, modos de juego variados y una jugabilidad realista.");

INSERT INTO usuarios (rol, usuario, contra, email, nombre, apellido, pais, ciudad, calle, direccion, codigo_postal) VALUES
('admin', 'admin', '1234', 'admin@example.com', 'Admin', 'Root', 'Argentina', 'CABA', 'Avenida Central', '123 Piso 1', '1000'),
('final', 'juancito', '4321', 'juan@gmail.com', 'Juan', 'Pérez', 'Argentina','AVELLANEDA', 'Mitre', '4325 Dto 3', '1407'),
('final', 'pepe', '5678', 'pepe@gmail.com', 'Pepe', 'Garcia', 'Argentina','San Isidro', 'Mitre', '4325 Dto 3', '1407'),
('final', 'carlos', '8910', 'carlos@gmail.com', 'Carlos', 'Aguas', 'Argentina','Palermo', 'Mitre', '4325 Dto 3', '1407');


INSERT INTO items_carrito (estado, usuario_id, juego_id, precio, tipo_envio) VALUES
('pendiente', 2, 1, 59.99, 'digital'),
('pendiente', 2, 2, 79.99, 'fisico'),
('comprado', 2, 3, 49.99, 'digital');

INSERT INTO metodos_pago (usuario_id, tipo, marca, numero_tarjeta, fecha_vencimiento, codigo_cvv) VALUES
(2, "TARJETA DEBITO", "VISA", "12345687", "2028-12-12", "321");