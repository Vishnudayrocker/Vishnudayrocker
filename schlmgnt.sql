--create database schlmgnt;
use schlmgnt;
--create table studentdetails_1(
--id int,age int,s_name varchar(20),dob date,phone int,primary key (id));
--create table parentdetails_1(
--p_name varchar(20),id int,phone int,foreign key (id) references studentdetails_1 (id),fee_id int,primary key (fee_id));
--create table teacherdetails(
--t_id int,t_name varchar(10),t_lastlogin date,primary key (t_id));
--create table schooldetails_1(
--s_name varchar(50),c_no int,id int,foreign key (id) references studentdetails_1 (id));
--create table classroomdetails_1(
--id int,section varchar(10),t_id int,foreign key (t_id) references teacherdetails (t_id),foreign key (id) references studentdetails_1 (id));
--create table attendancedetails_1(
--id int,foreign key (id) references studentdetails_1 (id),avg_attendance int,eligible varchar(10),primary key(eligible));
--create table stu_eligibility_1(
--id int,foreign key (id) references studentdetails_1 (id),sub varchar(60),marks int,eligible varchar(10),fee_id int,foreign key (fee_id) references parentdetails_1 (fee_id));
--create table exam_details(
--id int,foreign key (id) references studentdetails_1 (id),marks int);
--create table teacher_attendance(
--t_id int,foreign key (t_id) references teacherdetails (t_id),last_login date);
create table studentremarks(
id int,foreign key (id) references studentdetails_1 (id),t_id int,foreign key (t_id) references teacherdetails (t_id),remarks varchar(10));






