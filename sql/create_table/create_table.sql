/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2018/10/22 17:23:41                          */
/*==============================================================*/


drop table if exists dm_group;

drop table if exists dm_groupmerber;

drop table if exists dm_pic;

drop table if exists dm_user;

/*==============================================================*/
/* Table: dm_group                                              */
/*==============================================================*/
create table dm_group
(
   groupid              bigint not null,
   groupname            varchar(512),
   invitecode           varchar(512),
   admin                varchar(1024),
   createdate           int,
   creator              varchar(255),
   summary              varchar(2048),
   primary key (groupid)
);

alter table dm_group comment '群组';

/*==============================================================*/
/* Table: dm_groupmerber                                        */
/*==============================================================*/
create table dm_groupmerber
(
   groupid              bigint not null,
   userid               bigint not null,
   jointime             int,
   invitor              varchar(255),
   primary key (groupid, userid)
);

alter table dm_groupmerber comment '群组成员';

/*==============================================================*/
/* Table: dm_pic                                                */
/*==============================================================*/
create table dm_pic
(
   picid                bigint not null,
   picname              varchar(1024),
   picgroup             bigint,
   creator              varchar(255),
   primary key (picid)
);

alter table dm_pic comment '图片信息';

/*==============================================================*/
/* Table: dm_user                                               */
/*==============================================================*/
create table dm_user
(
   userid               bigint not null,
   username             varchar(255),
   pwd                  varchar(255),
   wechat_id            varchar(255),
   primary key (userid)
);

alter table dm_user comment '用户信息表';

