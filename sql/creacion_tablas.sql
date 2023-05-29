


CREATE TABLE public.year_dim 
(
	id SERIAL PRIMARY KEY,
	years INT UNIQUE NOT NULL,
	id_year INT UNIQUE NOT NULL

);


CREATE TABLE public.localidad_dim 
(
	id SERIAL PRIMARY KEY,
	localidad VARCHAR(300) UNIQUE NOT NULL,
	id_localidad INT UNIQUE NOT NULL

);


CREATE TABLE public.asma_dim 
(
	id SERIAL PRIMARY KEY,
	asma VARCHAR(100) UNIQUE NOT NULL,
	id_asma INT UNIQUE NOT NULL

);


CREATE TABLE public.vivienda_dim 
(
	id SERIAL PRIMARY KEY,
	id_vivienda INT UNIQUE NOT NULL,
	id_casa INT UNIQUE NOT NULL

);



CREATE TABLE public.hacinamiento_fact 
(
	id SERIAL PRIMARY KEY,
	hacinamiento FLOAT NOT NULL,
	cantidad_personas INT NOT NULL,
	cantidad_cuartos INT NOT NULL,
	cantidad_asma INT NOT NULL,
	porcentaje_luz_natural FLOAT NOT NULL,
	
	id_asma INT REFERENCES asma_dim (id_asma),
	id_year INT REFERENCES year_dim (id_year),
	id_localidad INT REFERENCES localidad_dim (id_localidad),
	id_vivienda INT REFERENCES vivienda_dim (id_vivienda)

);





