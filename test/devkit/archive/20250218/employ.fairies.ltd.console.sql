/*****************************************************
 * @software: PyCharm
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @datetime: 2025-02-18 20:33:16 UTC+08:00
 *****************************************************/

drop database if exists py_study;
drop table if exists example_user_info_1;

create database if not exists py_study char set utf8mb4;

use py_study;

create table if not exists example_user_info_1 (
	id         int auto_increment
		primary key comment 'ID',
	name       varchar(10) not null comment '姓名',
	account    varchar(16) not null
		unique comment '账号',
	department varchar(15) not null comment '部门',
	created_at timestamp default current_timestamp comment '创建时间',
	updated_at timestamp default current_timestamp on update current_timestamp comment '更新时间',
	existed    boolean   default true comment '是否存在'
);

insert into example_user_info_1 (name, account, department) value ('侯淼', 'houmiao', '研发部');
