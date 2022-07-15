create schema "my_gaming_plataform";

set schema 'my_gaming_plataform';

create table region (
	id_region serial4 not null PRIMARY KEY,
	name_region varchar(40) not null,
	acronym_region varchar(3) not null
);

CREATE TABLE my_gaming_plataform.game (
	id_game serial4 NOT null PRIMARY KEY,
	name_game varchar(60) NOT NULL,
	price numeric NOT NULL DEFAULT 0.0,
	release_date date NULL,
	producer varchar(50) NULL,
	category varchar(100),
	available bool not NULL DEFAULT false
);


create table my_gaming_plataform.user_tb (
	id_user serial4 not null PRIMARY KEY,
	user_name varchar(50) null default 'unknown',
	nick_name varchar(20) not null unique,
	email varchar(100) not null unique,
	passwd varchar(82) not null,
	id_region int4 references region(id_region),
	last_login date not null default CURRENT_DATE,
	date_join date not null default CURRENT_DATE,
	active bool not null default true
);

create table game_library (
	id_user int4 references user_tb(id_user),
	id_game int4 references game(id_game),
	date_add_library date not null default CURRENT_DATE
);


insert into region(id_region, name_region, acronym_region) values 
(1, 'south and central america', 'sa'),
(2, 'north america', 'na'),
(3, 'europe', 'eu'), 
(4, 'africa', 'af'),
(5, 'antarctica', 'an'),
(6, 'asia', 'as'),
(7, 'oceania', 'oc')
;