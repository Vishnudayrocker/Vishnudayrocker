--create database  deliverylist;
--use deliverylist;
--create table table1(cid int,name varchar(25),age int,contact int,adresss varchar(225), primary key(cid));
select * from table1;
--insert into table1
--(cid,name,age,contact,adresss)
--values(1856,'rahul',24,9656210,'xxxxxxx yyyyy');
--create table table2(
--id int not null,orderdetails varchar(255),price int,cid int,primary key(id),foreign key(cid) references table1(cid));
select * from table2;
--insert into table2(id,orderdetails,price,cid)
--values(34,'fkyujgfuk',75,1856);
