--create database hspital_details1;
use hspital_details1;
--create table access_2(
--ic varchar(50),
--password varchar(12),
--status varchar(20),
--cardlost varchar(20),
--primary key(ic));
select column_name access
from INFORMATION_SCHEMA.COLUMNS
where table_name='access_2'
order by ORDINAL_POSITION
--create table personal_4(
--name varchar(20),
--ic varchar(50),
--dob datetime,
--nationality varchar(25),
--age int,sex varchar(5),oocupation varchar(20),telhome int not null,telwork varchar(15),telmobile int not null,address varchar(50),photo varchar(5),height int,weight int,contactic varchar(50),foreign key (ic) references access_2 (ic),primary key(contactic,ic)); 
select column_name personal
from INFORMATION_SCHEMA.COLUMNS
where table_name='personal_4'
order by ORDINAL_POSITION