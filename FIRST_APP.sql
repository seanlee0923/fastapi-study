create database if not exists FIRST_APP
       default character set utf8mb4
       default collate utf8mb4_unicode_ci;

create table user
(
    id int auto_increment primary key,
    username varchar(255) not null default '',
    password varchar(255) not null,
    name varchar(255) not null,
    constraint username_UNK unique (username)
) collate = utf8mb4_bin;

create table post
(
    id int auto_increment primary key,
    title varchar(255) not null default '',
    content longtext not null,
    created_at timestamp default CURRENT_TIMESTAMP,
    user_id int not null
) collate = utf8mb4_bin;