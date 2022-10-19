--create database pushpa2;
use pushpa2;
--create table actor(
--act_id int,act_fname char(20),act_iname char(20),act_gender char(1),primary key (act_id));
--create table director(
--dir_id int,dir_fname char(20),dir_iname char(20),primary key (dir_id));
--create table movie(
--mov_id int,mov_title char(50),mov_year int,mov_time int,mov_lang char(50),mov_dt_rel date,mov_rel_country char(5),primary key (mov_id));
--create table reviewer(
--rev_id int,rev_name char(30),primary key(rev_id));
--create table genres(
--gen_id int,gen_title char (20),primary key(gen_id));


--create table movie_direction_1(
--dir_id int,mov_id int,foreign key(dir_id) references director (dir_id),foreign key(mov_id) references movie (mov_id));

create table moviecast_1(
act_id int,mov_id int,rolee char(20),foreign key(act_id) references actor(act_id),foreign  key(mov_id) references 
movie(mov_id));
--create table movie_genres(
--mov_id int,gen_id int,foreign key(mov_id) references movie (mov_id),foreign key(gen_id) references genres(gen_id));
--create table rating(
--mov_id int,foreign key(mov_id) references movie (mov_id),rev_id int,foreign key(rev_id) references reviewer(rev_id),rev_stars int,num_o_ratings int);