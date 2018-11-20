create database if not exists LR_DB Character set UTF8;
use LR_DB;
drop procedure if exists pro_add_user;
DELIMITER$$
create procedure pro_add_user()
BEGIN
declare icnt int default 0;
select count(*) into icnt from mysql.user where user = 'lr';
if icnt = 1
then drop user 'lr'@'%';
end if;
create user 'lr'@'%' identified by 'temp';
grant all privileges on LR_DB.* to 'lr'@'%' with grant option;
flush privileges;
END$$

call pro_add_user;
