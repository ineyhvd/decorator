create table person(
    full_name varchar(50),
    age int
);

alter table person
add column id serial primary key;

insert into person(full_name, age)
values('john doe',22),
      ('tursunxon tursonboyev',11),
      ('ali valiyev',44);