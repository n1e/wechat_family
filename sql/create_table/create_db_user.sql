create database if not exists LR_DB Character set UTF8;
drop user 'lr'@'%';
create user 'lr'@'%' identified by 'temp';

grant all privileges on LR_DB.* to 'lr'@'%' with grant option;
flush privileges;
